def print_top_entries(counter, n):
    """Prints the n most common entries in a frequency-counter dictionary"""
    top = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0:n]
    for entry in top:
        print(f'  {entry[1]:>3d} {entry[0]}')


dataset = 'hyperskill-dataset-118969053.txt'
start_time = '15:00'
end_time = '15:30'

full_counter = {}
timeframe_counter = {}

with open(dataset) as file:
    for line in file:
        time, error = line.split()
        full_counter[error] = full_counter.get(error, 0) + 1
        if start_time <= time and time <= end_time:
            timeframe_counter[error] = timeframe_counter.get(error, 0) + 1

print('Top 3 errors overall:')
print_top_entries(full_counter, 3)

print('\nTop 3 errors within timeframe:')
print_top_entries(timeframe_counter, 3)
