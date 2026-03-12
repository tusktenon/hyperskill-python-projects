import csv
import re

import pandas as pd

filename, extension = input('Input file name\n').rsplit('.', maxsplit=1)

if extension not in ('csv', 'xlsx'):
    print('Unknown file extension:', extension)
    exit(1)

src_filename = filename + '.csv'
dest_filename = filename + '[CHECKED].csv'

if extension == 'xlsx':
    df = pd.read_excel(filename + '.xlsx', sheet_name='Vehicles', dtype=str)
    df.to_csv(src_filename, index=False)
    print(f'{len(df)} line{" was" if len(df) == 1 else "s were"} imported to {src_filename}')

with open(src_filename, newline='') as src:
    with open(dest_filename, 'w', newline='') as dest:
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
            f'{corrected} cell{" was" if corrected == 1 else "s were"} corrected in {dest_filename}'
        )

