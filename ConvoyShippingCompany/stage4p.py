import csv
import re
import sqlite3

import pandas as pd


def xlsx_to_csv(src, dst):
    df = pd.read_excel(src, sheet_name='Vehicles', dtype=str)
    df.to_csv(dst, index=False)
    return len(df)


def check_csv(src, dst):
    with open(src, newline='') as src_file:
        with open(dst, 'w', newline='') as dst_file:
            src_reader = csv.reader(src_file, delimiter=',')
            dst_writer = csv.writer(dst_file, delimiter=',', lineterminator='\n')
            header_row = True
            corrected = 0
            for row in src_reader:
                if header_row:
                    dst_writer.writerow(row)
                    header_row = False
                    continue
                corrected_row = []
                for cell in row:
                    number = re.search(r'\d+', cell).group()
                    corrected_row.append(number)
                    if cell != number:
                        corrected += 1
                dst_writer.writerow(corrected_row)
            return corrected


def create_convoy_table(conn, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS convoy (
            vehicle_id INTEGER PRIMARY KEY,
            engine_capacity INTEGER NOT NULL,
            fuel_consumption INTEGER NOT NULL,
            maximum_load INTEGER NOT NULL
        )
    """)
    conn.commit()


def fill_table(conn, cursor, src):
    with open(src, newline='') as src_file:
        reader = csv.reader(src_file, delimiter=',')
        header_row = True
        inserted = 0
        for row in reader:
            if header_row:
                header_row = False
                continue
            cursor.execute('INSERT INTO convoy VALUES (?, ?, ?, ?)', tuple(row))
            inserted += 1
    conn.commit()
    return inserted


def sql_to_json(src, dst):
    with sqlite3.connect(src) as conn:
        df = pd.read_sql_query('SELECT * FROM convoy', conn)
        json_str = df.to_json(None, orient='records')
        with open(dst, 'w') as dst_file:
            dst_file.write('{"convoy":' + json_str + '}')
        return len(df)


def main():
    filename, extension = input('Input file name\n').rsplit('.', maxsplit=1)

    if extension not in ('csv', 'xlsx', 's3db'):
        print('Unsupported file type:', extension)
        exit(1)
    if extension == 'xlsx':
        src = filename + '.xlsx'
        dst = filename + '.csv'
        lines = xlsx_to_csv(src, dst)
        print(f'{lines} line{" was" if lines == 1 else "s were"} imported to {dst}')
        extension = 'csv'
    if extension == 'csv' and not filename.endswith('[CHECKED]'):
        src = filename + '.csv'
        dst = filename + '[CHECKED].csv'
        corrected = check_csv(src, dst)
        print(f'{corrected} cell{" was" if corrected == 1 else "s were"} corrected in {dst}')
        filename += '[CHECKED]'
    if extension == 'csv' and filename.endswith('[CHECKED]'):
        src = filename + '.csv'
        dst = filename.removesuffix('[CHECKED]') + '.s3db'
        with sqlite3.connect(dst) as conn:
            cursor = conn.cursor()
            create_convoy_table(conn, cursor)
            inserted = fill_table(conn, cursor, src)
            print(f'{inserted} record{" was" if inserted == 1 else "s were"} inserted into {dst}')
        filename = filename.removesuffix('[CHECKED]')
        extension = '.s3db'

    src = filename + '.s3db'
    dst = filename + '.json'
    saved = sql_to_json(src, dst)
    print(f'{saved} vehicle{" was" if saved == 1 else "s were"} saved in {dst}')


if __name__ == '__main__':
    main()
