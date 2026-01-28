capacity = int(input())
applicants = set()
with open('applicants.txt') as file:
    for line in file:
        name, gpa, first, second, third = line.rsplit(maxsplit=4)
        applicants.add((name, float(gpa), first, second, third))
sorted_applicants = sorted(list(applicants), key=lambda x: (-x[1], x[0]))
accepted = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

for priority in range(2, 5):
    for applicant in sorted_applicants:
        department = applicant[priority]
        if len(accepted[department]) < capacity and applicant in applicants:
            accepted[department].append(applicant)
            applicants.remove(applicant)

for department, students in accepted.items():
    # Hyperskill tests require the printed lists of accepted students
    # for each department to be sorted
    students.sort(key=lambda x: (-x[1], x[0]))
    print('\n' + department)
    print(*[f'{student[0]} {student[1]}' for student in students], sep='\n')
