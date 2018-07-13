'''
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
'''
import random
import time

def max_3_prod(nums):
	'''
	Maintain largest current product of 3, 2 and 1 through each step
	'''
	if len(nums) < 3:
		raise ValueError('List must have at least 3 elements to find the largest product of 3.')
	max_3_prod = nums[0] * nums[1] * nums[2]
	max_2_prod = nums[0] * nums[1]
	min_2_prod = nums[0] * nums[1]
	max_num = max(nums[0], nums[1])
	min_num = min(nums[0], nums[1])

	for m in nums[2:]:
		max_3_prod = max(max_3_prod, min_2_prod * m, max_2_prod * m)

		max_2_prod = max(max_num * m, min_num * m, max_2_prod)
		min_2_prod = min(max_num * m, min_num * m, min_2_prod)

		max_num = max(max_num, m)
		min_num = min(min_num, m)

	return max_3_prod

def max_3_prod2(nums):
	'''
	Keep track of largest and smallest numbers. Compute largest value at the end. 

	This algorithm saves considerable time compared to the first solution by 
	only performing two comparisons if a value is less extreme than the least
	extreme stored values. The first solution must perform each max comparison
	on each iteration which requires at least 8 comparisons. 
	'''
	if len(nums) < 3:
		raise ValueError('List must have at least 3 elements to find the largest product of 3.')
	max_3 = sorted(nums[0:3])
	min_2 = sorted(nums[0:2], reverse=True)

	insert_extreme(min_2, nums[2], False)

	for m in nums[3:]:
		insert_extreme(max_3,m,True)
		insert_extreme(min_2,m,False)
	return max(max_3[2] * max_3[1] * max_3[0], min_2[1] * min_2[0] * max_3[2])

def insert_extreme(vals, new, max1):
	if (new > vals[0]) == max1:
		i = 1
		while i < len(vals) and (new > vals[i])==max1:
			i += 1
		vals.insert(i,new)
		vals.pop(0)

def max_3_prod3(nums):
	'''
	This version removes the function call to insert extreme which saves more
	time.
	'''
	if len(nums) < 3:
		raise ValueError('List must have at least 3 elements to find the largest product of 3.')
	max_3 = sorted(nums[0:3])
	min_2 = sorted(nums[0:2], reverse=True)

	insert_extreme(min_2, nums[2], False)

	for m in nums[3:]:
		if (m > max_3[0]):
			i = 1
			while i < len(max_3) and (m > max_3[i]):
				i += 1
			max_3.insert(i,m)
			max_3.pop(0)

		elif (m < min_2[0]):
			i = 1
			while i < len(min_2) and (m < min_2[i]):
				i += 1
			min_2.insert(i,m)
			min_2.pop(0)

	return max(max_3[2] * max_3[1] * max_3[0], min_2[1] * min_2[0] * max_3[2])

def test():
	time1 = []
	time2 = []
	time3 = []
	for i in range(600):
		a = [random.randint(-1000,1000) for _ in range(random.randint(3,50))]
		
		start = time.time()
		c = max_3_prod2(a)
		end = time.time()
		time2.append(end - start)

		start = time.time()
		b = max_3_prod(a)
		end = time.time()
		time1.append(end - start)

		start = time.time()
		d = max_3_prod3(a)
		end = time.time()
		time3.append(end - start)

		if b != c or d != c:
			print(a,b,c)
			return

	print(sum(time1))
	print(sum(time2))
	print(sum(time3))

# print(max_3_prod2([2, 30, 34, -2, -14]))
# print(max_3_prod([2, 30, 34, -2, -14]))
test()
# print(max_3_prod([1,2,3,4,5]))
# print(max_3_prod([0,1,-6,5]))
# print(max_3_prod([-1,-2,-3,-4]))
# print(max_3_prod([-1,-2,0,-3,-4]))
# print(max_3_prod([1,-2,-3,-4]))
# print(max_3_prod([1,3,8,2,-2,-6,-5,-3]))


