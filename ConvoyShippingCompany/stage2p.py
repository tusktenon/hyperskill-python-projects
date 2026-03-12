import pandas as pd

filename, extension = input('Input file name\n').rsplit('.', maxsplit=1)

if extension not in ('csv', 'xlsx'):
    print('Unsupported file type:', extension)
    exit(1)

unchecked = filename + '.csv'
checked = filename + '[CHECKED].csv'

if extension == 'xlsx':
    df = pd.read_excel(filename + '.xlsx', sheet_name='Vehicles', dtype=str)
    df.to_csv(unchecked, index=False)
    print(f'{len(df)} line{" was" if len(df) == 1 else "s were"} imported to {unchecked}')

original = pd.read_csv(unchecked).astype(str)
corrected = original.replace(r'\D', '', regex=True)
corrections = (original != corrected).to_numpy().sum()
corrected.to_csv(checked, index=False)
print(f'{corrections} cell{" was" if corrections == 1 else "s were"} corrected in {checked}')
