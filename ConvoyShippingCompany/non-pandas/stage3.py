import csv
import re
import sqlite3

import pandas as pd


def xlsx_to_csv(src_file, dest_file):
    df = pd.read_excel(src_file, sheet_name='Vehicles', dtype=str)
    df.to_csv(dest_file, index=False)
    print(f'{len(df)} line{" was" if len(df) == 1 else "s were"} imported to {dest_file}')


def check_csv(src_file, dest_file):
    with open(src_file, newline='') as src:
        with open(dest_file, 'w', newline='') as dest:
            src_reader = csv.reader(src, delimiter=',')
            dest_writer = csv.writer(dest, delimiter=',', lineterminator='\n')
            header_row = True
            corrected = 0
            for row in src_reader:
                if header_row:
                    dest_writer.writerow(row)
                    header_row = False
                    continue
                corrected_row = []
                for cell in row:
                    number = re.search(r'\d+', cell).group()
                    corrected_row.append(number)
                    if cell != number:
                        corrected += 1
                dest_writer.writerow(corrected_row)
            print(
                f'{corrected} cell{" was" if corrected == 1 else "s were"} corrected in {dest_file}'
            )


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


def fill_table(conn, cursor, src_file):
    with open(src_file, newline='') as src:
        reader = csv.reader(src, delimiter=',')
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


def main():
    filename, extension = input('Input file name\n').rsplit('.', maxsplit=1)

    if extension not in ('csv', 'xlsx'):
        print('Unsupported file type:', extension)
        exit(1)
    if extension == 'xlsx':
        xlsx_to_csv(filename + '.xlsx', filename + '.csv')
    if not filename.endswith('[CHECKED]'):
        check_csv(filename + '.csv', filename + '[CHECKED].csv')

    datafile = filename.removesuffix('[CHECKED]') + '.s3db'
    csv_source = filename.removesuffix('[CHECKED]') + '[CHECKED].csv'
    with sqlite3.connect(datafile) as conn:
        cursor = conn.cursor()
        create_convoy_table(conn, cursor)
        inserted = fill_table(conn, cursor, csv_source)
        print(f'{inserted} record{" was" if inserted == 1 else "s were"} inserted into {datafile}')


if __name__ == '__main__':
    main()
