import json

data = json.loads(input())
errors = {
    field: 0 for field in ('bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time')
}

for stop in data:
    if not isinstance(stop['bus_id'], int):
        errors['bus_id'] += 1
    if not isinstance(stop['stop_id'], int):
        errors['stop_id'] += 1
    if not isinstance(stop['stop_name'], str) or not stop['stop_name']:
        errors['stop_name'] += 1
    if not isinstance(stop['next_stop'], int):
        errors['next_stop'] += 1
    if not isinstance(stop['stop_type'], str) or len(stop['stop_type']) > 1:
        errors['stop_type'] += 1
    if not isinstance(stop['a_time'], str) or not stop['a_time']:
        errors['a_time'] += 1

print(f'Type and field validation: {sum(errors.values())} errors')
print(*[f'{error}: {count}' for error, count in errors.items()], sep='\n')
