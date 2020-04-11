#Messy Salary into integers.

salary=['$876,001']
print([int(''.join(s[1:].split(',')))for s in salary])
