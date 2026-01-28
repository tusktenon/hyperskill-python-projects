DEPARTMENTS = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']

capacity = int(input())
applicants = set()
with open('applicants.txt') as file:
    for line in file:
        name, gpa, first, second, third = line.rsplit(maxsplit=4)
        applicants.add((name, float(gpa), first, second, third))
accepted = [[] for _ in DEPARTMENTS]

for priority in range(3):
    if not applicants or min([len(a) for a in accepted]) >= capacity:
        break
    rankings = [[] for _ in DEPARTMENTS]
    for applicant in applicants:
        rankings[DEPARTMENTS.index(applicant[priority + 2])].append(applicant)
    for department_ranking in rankings:
        department_ranking.sort(key=lambda x: (-x[1], x[0]))
    for i in range(len(DEPARTMENTS)):
        for j in range(min(capacity - len(accepted[i]), len(rankings[i]))):
            accepted[i].append(rankings[i][j])
            applicants.remove(rankings[i][j])

# Hyperskil tests require the lists of accepted students for each department
# to be sorted (by GPA, then name)
for department_acceptances in accepted:
    department_acceptances.sort(key=lambda x: (-x[1], x[0]))

for i, department in enumerate(DEPARTMENTS):
    print('\n' + department)
    for student in accepted[i]:
        print(student[0], student[1])
