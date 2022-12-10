n_m = list(map(int, input().split()))
attendees = []
n = n_m[0]
m = str(n_m[1])
for i in range(n):
    attendees.append(input())

dec_attendees = [int(n,2) for n in attendees]
result = {}
for i in range(1,n+1):
    for j in range(i+1, n+1):
        # print(i, j)
        binary_or = '{0:b}'.format(dec_attendees[i-1]|dec_attendees[j-1])
        result[(i,j)] = str(binary_or).count('1')
# print(result)
max_result = 0
for key, value in result.items():
    if value>max_result:
        max_result = value
print(max_result)
count = 0
for key, value in result.items():
    if value == max_result:
        count+=1
print(count)