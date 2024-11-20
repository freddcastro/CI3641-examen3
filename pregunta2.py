from math import floor

X = 7
Y = 8
Z = 3

L1 = min(X,Y)
L2 = min(X,Z)
L3 = min(Y,Z)

U1 = max(X,Y) + 1
U2 = max(X,Z) + 1
U3 = max(Y,Z) + 1

I = floor((L1+U1)/2)
J = floor((L2+U2)/2)
K = floor((L3+U3)/2)

# Valores para row_major
S3 = 4
S2 = (U3 - L3 + 1) * S3
S1 = (U2 - L2 + 1) * S2

# Calculamos la direccción M[I][J][K] en row_major
row_major = ((I - L1) * S1) + ((J - L2) *  S2) + ((K - L3) * S3)
print("el row major es")
print(row_major)

# Valores para column_major
S1 = 4
S2 = (U1 - L1 + 1) * S1
S3 = (U2 - L2 + 1) * S2


# Calculamos la direccción M[I][J][K] en column_major
column_major = ((I - L1) * S1) + ((J - L2) *  S2) + ((K - L3) * S3)
print("el column major es")
print(column_major)