total_applicants = int(input('Total number of applicants: '))
total_available = int(input('Number of applicants that can be accepted: '))

applicants = []
for _ in range(total_applicants):
    first, last, gpa = input().split()
    applicants.append((first, last, float(gpa)))

applicants.sort(key=lambda x: (-x[2], x[0], x[1]))

print('Successful applicants:')
for first, last, gpa in applicants[:total_available]:
    print(first, last)
