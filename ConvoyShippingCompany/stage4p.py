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
    types = {
        col: 'INTEGER PRIMARY KEY' if col == 'vehicle_id' else 'INTEGER NOT NULL'
        for col in df.columns
    }
    with sqlite3.connect(dst) as conn:
        df.to_sql('convoy', conn, index=False, dtype=types)
    print(f'{len(df)} record{" was" if len(df) == 1 else "s were"} inserted into {dst}')


def sql_to_json(src, dst):
    with sqlite3.connect(src) as conn:
        df = pd.read_sql_query('SELECT * FROM convoy', conn)
        json_str = df.to_json(None, orient='records')
        with open(dst, 'w') as dst_file:
            dst_file.write('{"convoy":' + json_str + '}')
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
        extension = '.s3db'

    src = filename + '.s3db'
    dst = filename + '.json'
    sql_to_json(src, dst)


if __name__ == '__main__':
    main()
