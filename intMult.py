'''
 You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution! 
'''
import random
import f_timer

def prod_all_except_curr_v2(nums):
	'''
	Final version which runs in O(n) and only uses one array
	'''
	if len(nums) < 2:
		raise ValueError('List must have at least two elements to show product of others')

	result = [1 for _ in nums]
	curr_prod = 1

	for i, n in enumerate(nums):
		curr_prod *= n
		result[i] = curr_prod

	curr_prod = 1
	for i in reversed(range(1,len(nums))):
		result[i] = result[i-1] * curr_prod
		curr_prod *= nums[i]
	result[0] = curr_prod

	return result


def prod_all_except_curr(nums):
	'''
	Version which runs in O(n) time but uses an extra array
	'''
	if len(nums) < 2:
		raise ValueError('List must have at least two elements to show product of others')
	left_prod = [1 for _ in nums]
	right_prod = 1
	result = [1 for _ in nums]
	left_prod[0] = nums[0]

	for i, n in enumerate(nums[1:]):		
		left_prod[i+1] = left_prod[i] * n

	for i in reversed(range(1,len(nums))):
		result[i] = left_prod[i-1] * right_prod
		right_prod *= nums[i]
	result[0] = right_prod

	return result


def naive_prod(nums):
	'''
	Initial naive O(n^2) algorith
	'''
	if len(nums) < 2:
		raise ValueError('Too short')

	products = [0 for i in nums]
	for i in range(len(nums)):
		product = 1
		for j in range(len(nums)):
			if j != i:
				product = product * nums[j]
		products[i] = product
	return products


def gen_rand_arr(largest_array, largest_int, smallest_int):
	return [[random.randint(-5,10) for _ in range(random.randrange(2,10))]]

print(f_timer.time_funcs([prod_all_except_curr, prod_all_except_curr_v2, naive_prod], gen_rand_arr, [10000,100,-50], 1000000))

# print(prod_all_except_curr_v2([1,2,3,4,5]))
# print(prod_all_except_curr_v2([1,7,3,4]))
# print(prod_all_except_curr_v2([1,7,3,4,0]))
# print(prod_all_except_curr_v2([1,7,3,-4,-3]))
# print(prod_all_except_curr_v2([-3,4,1,2,5]))



