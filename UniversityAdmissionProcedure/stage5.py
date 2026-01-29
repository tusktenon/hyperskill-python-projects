CRITERIA = {
    'physics': ('Physics',),
    'chemistry': ('Biotech', 'Chemistry'),
    'math': ('Mathematics',),
    'computer_science': ('Engineering',),
}

capacity = int(input())

applicants = set()
with open('data/stage5/example.txt') as file:
    for line in file:
        name, phy, chem, math, cs, first, second, third = line.rsplit(maxsplit=7)
        applicants.add(
            (name, float(phy), float(chem), float(math), float(cs), first, second, third)
        )

sorted = {
    exam: sorted(list(applicants), key=lambda x: (-x[i], x[0]))
    for i, exam in enumerate(CRITERIA.keys(), start=1)
}

accepted = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

for priority in range(5, 8):
    for i, exam in enumerate(CRITERIA.keys(), start=1):
        for applicant in sorted[exam]:
            if (
                (preference := applicant[priority]) in CRITERIA[exam]
                and len(accepted[preference]) < capacity
                and applicant in applicants
            ):
                accepted[preference].append((applicant[0], applicant[i]))
                applicants.remove(applicant)

for department, students in accepted.items():
    students.sort(key=lambda x: (-x[1], x[0]))
    print('\n' + department)
    print(*[f'{student[0]} {student[1]}' for student in students], sep='\n')
