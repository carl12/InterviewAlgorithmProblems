'''
Array Quadruplet

Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

------------------------


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
          # print(i,j,k,l)
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
	counter = 0
	if not arr or len(arr) < 4:
		return []
	arr.sort();
	sums = collections.OrderedDict();
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			counter += 1
			if arr[i] + arr[j] not in sums:
				sums[arr[i]+arr[j]] = [(i,j)]
			else:
				sums[arr[i]+arr[j]].append((i,j))

	sol = None
	found = 0
	for sum1 in sums.keys():
		counter+=1
		if(s-sum1) in sums:
			pairs1 = sums[sum1]
			pairs2 = sums[s-sum1]
			if not sol or pairs1[0][0] <= sol[0]:
				for i in range(len(pairs1)):
					if sol and list(pairs1[i]) > sol[0:2]:
						break
					pair1 = pairs1[i]
					for pair2 in pairs2:
						if sol and list(pairs1[i]) == sol[0:2] and list(pair2) > sol[2:4]:
							break
						counter += 1
						if(pair1[0] not in pair2 and pair1[1] not in pair2):
							new = sorted([pair1[0], pair1[1], pair2[0], pair2[1]])
							found +=1
							# return sorted([arr[pair1[0]], arr[pair1[1]], arr[pair2[0]], arr[pair2[1]]])
							# if(found < 20):
							# 	print(new)
							sol = new if not sol or new < sol else sol
			else:
				
				# print('-~~-')
				if(counter > len(arr)**2):
				# 	print(arr)
				# 	print(s)
				# 	print(sol)
					print('asdf')
					print(counter , len(arr)**2)
				# 	print(len(sums[s-(sol[0]+sol[1])]))
				# 	print(len(sums[s-(sol[2]+sol[3])]))
				# print(len(arr))
				# print("solutions ", found)
				# print('---')
				return [arr[i] for i in sol]

	if(counter > len(arr)**2):
		print('asdf')
		print(counter, len(arr)**2)
	# 	print(arr)
	# 	print('didnt even find anything!')
	# print(counter)
	return [arr[i] for i in sol] if sol else []



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

def find_array_quadruplet5(arr, s):
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

	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			sum1 = arr[i]+arr[j]
			if (s - sum1) in sums:
				pairs = sums[s-sum1]
				for pair2 in pairs:
					if(i != pair2[0] and j != pair2[0] and i != pair2[1] and j != pair2[1]):
						return sorted([arr[i],arr[j],arr[pair2[0]],arr[pair2[1]]])

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


a = [-3687, -3683, -3665, -3584, -3373, -3335, -3274, -3221, -3189, -3010, -2879, -2744, -2668, -2649, -2592, -2570, -2457, -2450, -2401, -2128, -2092, -2048, -1982, -1973, -1721, -1664, -1619, -1601, -1109, -1033, -960, -948, -928, -908, -902, -818, -788, -782, -673, -665, -638, -569, -296, -241, -219, -111, 193, 260, 453, 520, 611, 675, 809, 822, 985, 1163, 1211, 1285, 1331, 1394, 1480, 1559, 1594, 1697, 1734, 1787, 1965, 1969, 2017, 2057, 2063, 2074, 2263, 2270, 2331, 2343, 2515, 2523, 2589, 2591, 2634, 2643, 2703, 2867, 2876, 2973, 2997, 3396, 3461, 3485, 3682, 3722, 3730]
target = 10597


# print(find_array_quadruplet(a, 17))
# print(find_array_quadruplet2(a, 17))
# print(find_array_quadruplet3(a, target))
# print(find_array_quadruplet(a,target))

algorithms = [find_array_quadruplet3, find_array_quadruplet4, find_array_quadruplet5]
# print(sorted([[1,2],[0,2],[3,5],[12,5],[0,0],[22,0]]))
# print(f_timer.time_funcs(algorithms, problem_builder, [100, 30000], 1000, True))
# print(f_timer.time_funcs(algorithms, problem_builder, [200, 30000], 1000, True))
# print(f_timer.time_funcs(algorithms, problem_builder, [400, 30000], 100, True))
print(f_timer.time_funcs(algorithms, problem_builder, [3200, 300000], 100, False))

# win = 0
# total = 100
# for i in range(total):
# 	if len(find_array_quadruplet3(*problem_builder(*[800,3000]))) > 0:
# 		win+=1

# print(win/total)


# target = sum([-375, -119, 373, 375])

# print(find_array_quadruplet3(a,target))