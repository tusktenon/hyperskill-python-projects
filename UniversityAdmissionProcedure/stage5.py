from collections import namedtuple
from enum import IntEnum

Applicant = namedtuple('Applicant', ['name', 'results', 'preferences'])
Exam = IntEnum('Exam', [('CHEM', 0), ('COMP_SCI', 1), ('MATH', 2), ('PHYSICS', 3)])

EXAMS = {
    'Biotech': Exam.CHEM,
    'Chemistry': Exam.CHEM,
    'Engineering': Exam.COMP_SCI,
    'Mathematics': Exam.MATH,
    'Physics': Exam.PHYSICS,
}

capacity = int(input())

applicants = set()
with open('data/stage5/example.txt') as file:
    for line in file:
        name, physics, chem, math, comp_sci, first, second, third = line.rsplit(maxsplit=7)
        results = (float(chem), float(comp_sci), float(math), float(physics))
        applicants.add(Applicant(name, results, (first, second, third)))

accepted = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

for priority in range(3):
    for department, exam in EXAMS.items():
        sorted_applicants = sorted(list(applicants), key=lambda x: (-x.results[exam], x.name))
        for applicant in sorted_applicants:
            preference = applicant.preferences[priority]
            if preference == department and len(accepted[preference]) < capacity:
                accepted[preference].append((applicant.name, applicant.results[exam]))
                applicants.remove(applicant)

for department, students in accepted.items():
    students.sort(key=lambda x: (-x[1], x[0]))
    print('\n' + department)
    print(*[f'{student[0]} {student[1]}' for student in students], sep='\n')
