total_applicants = int(input('Total number of applicants: '))
total_available = int(input('Number of applicants that can be accepted: '))

applicants = [input().rsplit(maxsplit=1) for _ in range(total_applicants)]
applicants.sort(key=lambda x: (-float(x[1]), x[0]))

print('Successful applicants:')
print(*[a[0] for a in applicants[:total_available]], sep='\n')
