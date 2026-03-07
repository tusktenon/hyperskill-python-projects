import pandas as pd

excel_filename = input('Input file name\n')
csv_filename = excel_filename.removesuffix('.xlsx') + '.csv'
df = pd.read_excel(excel_filename, sheet_name='Vehicles', dtype=str)
df.to_csv(csv_filename, index=False)
print(f'{len(df)} line{" was" if len(df) == 1 else "s were"} imported to {csv_filename}')

