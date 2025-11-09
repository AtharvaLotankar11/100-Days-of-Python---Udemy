student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)

# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)

# print(max(student_scores)) - 199
# print(min(student_scores)) - 24

maxm = 0
minm = student_scores[0]

for score in student_scores:
    if score > maxm:
        maxm = score
    if score <= minm:
        minm = score

print(maxm)
print(minm)
