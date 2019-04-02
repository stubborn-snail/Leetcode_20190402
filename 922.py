def sortArrayByParityII(A):
	A_odd = []
	A_even = []
	A_final = []
	for i in A:
		if i%2 == 0:
			A_odd.append(i)
		if i%2 == 1:
			A_even.append(i)
	for i in range(len(A)):
		if i%2 == 0:
			A_final.append(A_odd[i//2])
		if i%2 == 1:
			A_final.append(A_even[i//2])
	return A_final

A = [4,2,5,7]
A_1=sortArrayByParityII(A)
print(A_1)