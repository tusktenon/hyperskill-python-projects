import sqlite3

import pandas as pd


def xlsx_to_csv(src, dst):
    df = pd.read_excel(src, sheet_name='Vehicles', dtype=str)
    df.to_csv(dst, index=False)
    print(f'{len(df)} line{" was" if len(df) == 1 else "s were"} imported to {dst}')


def check_csv(src, dst):
    original = pd.read_csv(src).astype(str)
    corrected = original.replace(r'\D', '', regex=True)
    corrections = (original != corrected).to_numpy().sum()
    corrected.to_csv(dst, index=False)
    print(f'{corrections} cell{" was" if corrections == 1 else "s were"} corrected in {dst}')


def csv_to_sql(src, dst):
    df = pd.read_csv(src)
    df['score'] = df.apply(score, axis=1)
    types = {
        col: 'INTEGER PRIMARY KEY' if col == 'vehicle_id' else 'INTEGER NOT NULL'
        for col in df.columns
    }
    with sqlite3.connect(dst) as conn:
        df.to_sql('convoy', conn, index=False, dtype=types)
    print(f'{len(df)} record{" was" if len(df) == 1 else "s were"} inserted into {dst}')


def score(row):
    stops = 4.5 // (row.engine_capacity / row.fuel_consumption)
    fuel_use = 4.5 * row.fuel_consumption
    stops_score = 2 if stops == 0 else 1 if stops == 1 else 0
    fuel_score = 2 if fuel_use <= 230 else 1
    capacity_score = 2 if row.maximum_load >= 20 else 0
    return stops_score + fuel_score + capacity_score


def sql_to_json(src, dst):
    with sqlite3.connect(src) as conn:
        df = pd.read_sql_query(
            """
            SELECT vehicle_id, engine_capacity, fuel_consumption, maximum_load 
            FROM convoy WHERE score > 3
        """,
            conn,
        )
    json_str = df.to_json(None, orient='records')
    with open(dst, 'w') as dst_file:
        dst_file.write('{"convoy":' + json_str + '}')
    print(f'{len(df)} vehicle{" was" if len(df) == 1 else "s were"} saved in {dst}')


def sql_to_xml(src, dst):
    with sqlite3.connect(src) as conn:
        df = pd.read_sql_query(
            """
            SELECT vehicle_id, engine_capacity, fuel_consumption, maximum_load 
            FROM convoy WHERE score <= 3
        """,
            conn,
        )
    if len(df):
        df.to_xml(dst, index=False, root_name='convoy', row_name='vehicle', xml_declaration=False)
    else:
        # in case of no rows, the pandas to_xml() method produces '<convoy/>'
        with open(dst, 'w') as dst_file:
            dst_file.write('<convoy></convoy>')
    print(f'{len(df)} vehicle{" was" if len(df) == 1 else "s were"} saved in {dst}')


def main():
    filename, extension = input('Input file name\n').rsplit('.', maxsplit=1)

    if extension not in ('csv', 'xlsx', 's3db'):
        print('Unsupported file type:', extension)
        exit(1)
    if extension == 'xlsx':
        src = filename + '.xlsx'
        dst = filename + '.csv'
        xlsx_to_csv(src, dst)
        extension = 'csv'
    if extension == 'csv' and not filename.endswith('[CHECKED]'):
        src = filename + '.csv'
        dst = filename + '[CHECKED].csv'
        check_csv(src, dst)
        filename += '[CHECKED]'
    if extension == 'csv' and filename.endswith('[CHECKED]'):
        src = filename + '.csv'
        dst = filename.removesuffix('[CHECKED]') + '.s3db'
        csv_to_sql(src, dst)
        filename = filename.removesuffix('[CHECKED]')

    src = filename + '.s3db'
    sql_to_json(src, filename + '.json')
    sql_to_xml(src, filename + '.xml')


if __name__ == '__main__':
    main()
