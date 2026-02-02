from typing import NamedTuple


class GradeSet(NamedTuple):
    chemistry: float
    comp_sci: float
    math: float
    physics: float
    special: float

    def score(self, department):
        return max(self.standard_score(department), self.special)

    def standard_score(self, department):
        match department:
            case 'Biotech':
                return (self.chemistry + self.physics) / 2
            case 'Chemistry':
                return self.chemistry
            case 'Engineering':
                return (self.comp_sci + self.math) / 2
            case 'Mathematics':
                return self.math
            case 'Physics':
                return (self.math + self.physics) / 2
            case _:
                raise ValueError('Unknown department')


class Applicant(NamedTuple):
    name: str
    grades: GradeSet
    preferences: tuple


def read_applicants(datafile):
    applicants = set()
    with open(datafile) as file:
        for line in file:
            columns = line.rsplit(maxsplit=8)
            name, physics, chemistry, math, comp_sci, special, first, second, third = columns
            grades = GradeSet(*map(float, (chemistry, comp_sci, math, physics, special)))
            applicants.add(Applicant(name, grades, (first, second, third)))
    return applicants


def process_applicants(applicants, capacity):
    accepted = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
    for priority in range(3):
        for department in accepted:
            sorted_applicants = sorted(
                list(applicants),
                key=lambda a: (-a.grades.score(department), a.name),
            )
            for applicant in sorted_applicants:
                preference = applicant.preferences[priority]
                if preference == department and len(accepted[preference]) < capacity:
                    accepted[preference].append(
                        (applicant.name, applicant.grades.score(department))
                    )
                    applicants.remove(applicant)
    for student_list in accepted.values():
        student_list.sort(key=lambda x: (-x[1], x[0]))
    return accepted


def write_student_lists(accepted):
    for department, students in accepted.items():
        print(department)
        print(*[f'{student[0]} {student[1]}' for student in students], sep='\n', end='\n\n')
        with open(department.lower() + '.txt', 'w') as file:
            file.writelines([f'{student[0]} {student[1]}\n' for student in students])


def main():
    capacity = int(input())
    applicants = read_applicants('data/stage7/extract.txt')
    accepted = process_applicants(applicants, capacity)
    write_student_lists(accepted)


if __name__ == '__main__':
    main()
