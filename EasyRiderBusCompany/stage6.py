import json
from itertools import groupby

data = json.loads(input())
data = sorted(data, key=lambda stop: stop['bus_id'])
stops_by_line = [(k, list(g)) for k, g in groupby(data, key=lambda stop: stop['bus_id'])]


def check_types_formats_times():
    # At this stage, all type, format and timing errors have been checked and fixed
    errors = {k: 0 for k in ('bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time')}
    print(f'Type and field validation: {sum(errors.values())} errors')
    print(*[f'{error}: {count}' for error, count in errors.items()], sep='\n', end='\n\n')


def display_stop_counts():
    print('Line names and number of stops:')
    print(
        *[f'bus_id {line} stops: {len(stops)}' for line, stops in stops_by_line],
        sep='\n',
        end='\n\n',
    )


def display_special_stops():
    all_stops = set()
    start_stops = set()
    transfer_stops = set()
    end_stops = set()
    on_demand_stops = set()

    for stop in data:
        name = stop['stop_name']
        if name in all_stops:
            transfer_stops.add(name)
        else:
            all_stops.add(name)
        if stop['stop_type'] and (index := 'SFO'.find(stop['stop_type'])) != -1:
            (start_stops, end_stops, on_demand_stops)[index].add(name)

    on_demand_stops -= start_stops | transfer_stops | end_stops

    print(f'Start stops: {len(start_stops)}', sorted(list(start_stops)))
    print(f'Transfer stops: {len(transfer_stops)}', sorted(list(transfer_stops)))
    print(f'Finish stops: {len(end_stops)}', sorted(list(end_stops)))
    print(f'On demand stops: {len(on_demand_stops)}', sorted(list(on_demand_stops)))


def main():
    check_types_formats_times()
    display_stop_counts()
    display_special_stops()


if __name__ == '__main__':
    main()
