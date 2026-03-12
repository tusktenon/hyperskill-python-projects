import sqlite3

import pandas as pd


def xlsx_to_csv(src_file, dest_file):
    df = pd.read_excel(src_file, sheet_name='Vehicles', dtype=str)
    df.to_csv(dest_file, index=False)
    print(f'{len(df)} line{" was" if len(df) == 1 else "s were"} imported to {dest_file}')


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


def main():
    filename, extension = input('Input file name\n').rsplit('.', maxsplit=1)

    if extension not in ('csv', 'xlsx'):
        print('Unsupported file type:', extension)
        exit(1)
    if extension == 'xlsx':
        xlsx_to_csv(filename + '.xlsx', filename + '.csv')
    if not filename.endswith('[CHECKED]'):
        check_csv(filename + '.csv', filename + '[CHECKED].csv')

    csv_source = filename.removesuffix('[CHECKED]') + '[CHECKED].csv'
    sql_datafile = filename.removesuffix('[CHECKED]') + '.s3db'
    csv_to_sql(csv_source, sql_datafile)


if __name__ == '__main__':
    main()
