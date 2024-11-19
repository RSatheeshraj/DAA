A = [[1, 7], [4, 2]]
B = [[6, 8], [3, 5]]
P1 = A[0][0] * (B[0][1] - B[1][1])
P2 = (A[0][0] + A[0][1]) * B[1][1]
P3 = (A[1][0] + A[1][1]) * B[0][0]
P4 = A[1][1] * (B[1][0] - B[0][0])
P5 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
P6 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])
P7 = (A[0][0] - A[1][0]) * (B[0][0] + B[0][1])
C = [
    [P5 + P4 - P2 + P6, P1 + P2],
    [P3 + P4, P1 + P5 - P3 - P7]
]
print("Product matrix C is:")
for row in C:
    print(row)
