import json
from itertools import groupby, pairwise

data = json.loads(input())
data = sorted(data, key=lambda stop: stop['bus_id'])
stops_by_line = [(k, list(g)) for k, g in groupby(data, key=lambda stop: stop['bus_id'])]


def check_types_formats_times():
    errors = {k: 0 for k in ('bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time')}

    # Type and format errors for bus_id, stop_name, stop_type and a_time have been checked and fixed
    for stop in data:
        if not isinstance(stop['stop_id'], int):
            errors['stop_id'] += 1
        if not isinstance(stop['next_stop'], int):
            errors['next_stop'] += 1

    for _, stops in stops_by_line:
        a_time_pairs = list(pairwise([stop['a_time'] for stop in stops]))
        errors['a_time'] += any([p[0] > p[1] for p in a_time_pairs])

    print(f'Type and field validation: {sum(errors.values())} errors')
    print(*[f'{error}: {count}' for error, count in errors.items()], sep='\n', end='\n\n')


def display_stop_counts():
    print('Line names and number of stops:')
    print(
        *[f'bus_id {line} stops: {len(stops)}' for line, stops in stops_by_line],
        sep='\n',
        end='\n\n',
    )


def check_start_end_stops():
    for line, all_stops in stops_by_line:
        has_start = any([stop['stop_type'] == 'S' for stop in all_stops])
        has_end = any([stop['stop_type'] == 'F' for stop in all_stops])
        if not has_start or not has_end:
            print('There is no start or end stop for the line:', line)
            return False
    return True


def display_special_stops():
    all_stops = set()
    start_stops = set()
    transfer_stops = set()
    end_stops = set()

    for stop in data:
        name = stop['stop_name']
        if name in all_stops:
            transfer_stops.add(name)
        else:
            all_stops.add(name)
        if stop['stop_type'] == 'S':
            start_stops.add(name)
        elif stop['stop_type'] == 'F':
            end_stops.add(name)

    print(f'Start stops: {len(start_stops)}', sorted(list(start_stops)))
    print(f'Transfer stops: {len(transfer_stops)}', sorted(list(transfer_stops)))
    print(f'Finish stops: {len(end_stops)}', sorted(list(end_stops)))


def main():
    check_types_formats_times()
    display_stop_counts()
    if check_start_end_stops():
        display_special_stops()


if __name__ == '__main__':
    main()
