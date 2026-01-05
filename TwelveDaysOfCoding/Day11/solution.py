from queue import PriorityQueue

DATASET = 'hyperskill-dataset-119229935.txt'
WORKERS = 11

debug = False
debug_simulation_loops = 10


### STEP 1: Read task durations and dependencies from the dataset

# Since tasks are indexed sequentially from 0, we can just use lists instead of dicts
durations = []
dependencies = []

with open(DATASET) as file:
    for line in file:
        _, duration, deps_str = line.rstrip().split(',')
        durations.append(int(duration))
        if deps_str == 'none':
            deps = []
        else:
            deps = deps_str.split(':')
            deps = [int(x) for x in deps]
        dependencies.append(deps)

tasks = len(durations)


### STEP 2: Calculate the critical path


def earliest_start(task):
    if dependencies[task]:
        return max([earliest_finish(x) for x in dependencies[task]])
    else:
        return 0


def earliest_finish(task):
    if dependencies[task]:
        return max([earliest_finish(x) for x in dependencies[task]]) + durations[task]
    else:
        return durations[task]


project_finish = max([earliest_finish(t) for t in range(tasks)])

# Build the list of each task's successors (the reverse index of the dependencies list)
successors = []
for task in range(tasks):
    successors.append([])
for task, deps in enumerate(dependencies):
    for d in deps:
        successors[d].append(task)


def latest_start(task):
    return latest_finish(task) - durations[task]


def latest_finish(task):
    if successors[task]:
        return min([latest_start(x) for x in successors[task]])
    else:
        return project_finish


critical_tasks = [t for t in range(tasks) if earliest_start(t) == latest_start(t)]
latest_starts = [latest_start(t) for t in range(tasks)]

if debug:
    print('Critical tasks:', critical_tasks)
print('Estimated project finish:', latest_finish(critical_tasks[-1]))

# In the next step, critical_tasks is more convenient as a set
critical_tasks = set(critical_tasks)


### STEP 3: Run the simulation

# Elapsed time
time = 0

# Times when each worker becomes available
busy_until = WORKERS * [0]

# Set of tasks that have yet to be completed
to_complete = set(range(tasks))


# Tests whether a task is available (all dependencies have been completed)
def is_startable(task):
    for d in dependencies[task]:
        if d in to_complete:
            return False
    return True


# Task priority function
def priority(task):
    return latest_starts[task] - 1_000 if task in critical_tasks else latest_starts[task]


loops = 0
while to_complete:
    if debug and loops < debug_simulation_loops:
        print('\nLoop', loops)
        print('Time:', time)
    # Find available workers, and mark their previous tasks as completed
    free_workers = set()
    for worker in range(WORKERS):
        if busy_until[worker] <= time:
            free_workers.add(worker)
    if debug and loops < debug_simulation_loops:
        print('Free workers:', free_workers)
        print(f'To_complete: {to_complete} ({len(to_complete)} tasks)')

    # Build queue of available tasks
    startable = PriorityQueue()
    for task in to_complete:
        if is_startable(task):
            startable.put((priority(task), task))

    # Assign tasks to workers
    while free_workers and not startable.empty():
        worker = free_workers.pop()
        _, task = startable.get()
        busy_until[worker] += durations[task]
        to_complete.discard(task)
        if debug and loops < debug_simulation_loops:
            print(f'Assigning task {task} to worker {worker}, now busy until {busy_until[worker]}')

    # Advance elapsed time until a worker becomes available
    time = min(busy_until)
    if debug and loops < debug_simulation_loops:
        print('Advancing time to', time)
    loops += 1

if debug:
    print()
print('Actual completion time:', max(busy_until))
