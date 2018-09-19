'''
Array Quadruplet

Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.
'''
import collections
import random
import f_timer

def find_array_quadruplet(arr, s):
  if(not arr or len(arr) < 4):
    return []
  arr.sort()
  
  for i in range(len(arr) - 3):
    for j in range(i+1,len(arr) - 2):
      desired_value = s - (arr[i] + arr[j])
      k = j+1
      l = len(arr)-1
      while(l > k):
        sum2 = arr[k] + arr[l]
        if desired_value > sum2:
          k+=1
        elif desired_value < sum2:
          l-=1
        else:	
          # print(i, j, len(arr))

          return [arr[i],arr[j],arr[k],arr[l]]
  return []

def find_array_quadruplet2(arr, s):
	if not arr or len(arr) < 4:
		return []
	arr.sort();
	solutions = []
	counter = 0

	sums = collections.OrderedDict();
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if i != j:
				# print(arr[i]+arr[j])
				if arr[i] + arr[j] not in sums:
					sums[arr[i]+arr[j]] = [(i,j)]
				else:
					sums[arr[i]+arr[j]].append((i,j))
	
	for sum1 in sums.keys():
		if(s-sum1) in sums:
			pairs1 = sums[sum1]
			pairs2 = sums[s-sum1]
			for pair1 in pairs1:
				for pair2 in pairs2:
					counter +=1
					if(pair1[0] not in pair2 and pair1[1] not in pair2):
						solutions.append(sorted([arr[pair1[0]], arr[pair1[1]], arr[pair2[0]], arr[pair2[1]]]))

	return sorted(solutions)[0] if len(solutions) > 0 else []

def find_array_quadruplet3(arr, s):
	if not arr or len(arr) < 4:
		return []
	arr.sort();
	sums = collections.OrderedDict();
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if i != j:
				# print(arr[i]+arr[j])
				if arr[i] + arr[j] not in sums:
					sums[arr[i]+arr[j]] = [(i,j)]
				else:
					sums[arr[i]+arr[j]].append((i,j))

	sol = None
	for sum1 in sums.keys():
		if(s-sum1) in sums:
			pairs1 = sums[sum1]
			pairs2 = sums[s-sum1]
			if not sol or arr[pairs1[0][0]] <= sol[0]:
				for i in range(len(pairs1)):
					pair1 = pairs1[i]
					for pair2 in pairs2:
						if(pair1[0] not in pair2 and pair1[1] not in pair2):
							new = sorted([arr[pair1[0]], arr[pair1[1]], arr[pair2[0]], arr[pair2[1]]])

							sol = new if not sol or new < sol else sol
			else:
				return sol

	return sol if sol else []



def find_array_quadruplet4(arr, s):
	if not arr or len(arr) < 4:
		return []
	arr.sort();

	sums = collections.OrderedDict();
	order = []
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if i != j:
				if arr[i] + arr[j] not in sums:
					sums[arr[i]+arr[j]] = [(i,j)]
				else:
					sums[arr[i]+arr[j]].append((i,j))
				order.append([i,j])
	matches = 0
	pairs = 0
	for pair1 in order:
		pairs = pairs + 1
		sum1 = arr[pair1[0]] + arr[pair1[1]]
		if (s - sum1) in sums:
			matches = matches + 1
			pairs2 = sums[s-sum1]
			for pair2 in pairs2:
				if(pair1[0] not in pair2 and pair1[1] not in pair2):
					return sorted([arr[pair1[0]], arr[pair1[1]], arr[pair2[0]], arr[pair2[1]]])


	return []

def problem_builder(maxLen, maxSum):
	arr_len = random.randint(4,maxLen)
	roll = random.randint(1,3)
	# if roll == 1:
	target_sum = random.randint(0, maxSum) #numbers could be negative
	random_arr = sorted([random.randint(-maxSum//8, maxSum//8) for _ in range(arr_len)])
	# elif roll == 2:
	# target_sum = maxSum
	# random_arr = [0 for _ in range(arr_len)]
	# elif roll == 3:
	# 	target_sum = random.randint(maxSum/2, maxSum)
	# 	random_arr = [random.randint(0, maxSum/4) for _ in range(arr_len)]

	return [random_arr, target_sum]


# a = [-28, -27, -21, -18, -16, -14, -12, -10, 1, 6, 12, 12, 18, 22, 23, 25, 28]

# print(find_array_quadruplet(a, 17))
# print(find_array_quadruplet2(a, 17))
# print(find_array_quadruplet3(a, 17))


# print(sorted([[1,2],[0,2],[3,5],[12,5],[0,0],[22,0]]))
print(f_timer.time_funcs([find_array_quadruplet, find_array_quadruplet4], problem_builder, [100, 30000], 100, True))
print(f_timer.time_funcs([ find_array_quadruplet, find_array_quadruplet4], problem_builder, [200, 30000], 100, True))
# print(f_timer.time_funcs([ find_array_quadruplet, find_array_quadruplet4], problem_builder, [300, 30000], 100, True))
print(f_timer.time_funcs([ find_array_quadruplet, find_array_quadruplet4], problem_builder, [400, 30000], 100, True))
print(f_timer.time_funcs([ find_array_quadruplet, find_array_quadruplet4], problem_builder, [800, 30000], 100, True))
# print(find_array_quadruplet2([2, 7, 4, 0, 9, 5, 1, 3], 20))


