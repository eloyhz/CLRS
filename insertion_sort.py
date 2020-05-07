# INSERTION-SORT(A)
# 1		for j = 2 to A.length
# 2			key = A[j]
# 3			// Insert A[j] into the sorted sequence A[1..j - 1]
# 4			i = j - 1
# 5			while i > 0 and A[i] < key
# 6				A[i + 1] = A[i]
# 7				i = i - 1
# 8			A[i + 1] = key


def insertion_sort(a):
	for j in range(len(a)):
		key = a[j]
		i = j - 1
		while i >= 0 and a[i] > key:
			a[i + 1] = a[i]
			i -= 1
		a[i + 1] = key


if __name__ == "__main__":
	# test = [5, 2, 4, 6, 1, 3]
	test = [31, 41, 59, 26, 41, 58]
	print("Before insertion sort: ", test)
	insertion_sort(test)
	print("After insertion sort: ", test)

