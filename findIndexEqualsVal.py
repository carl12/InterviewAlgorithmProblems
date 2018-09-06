'''
Given a sorted array arr of distinct integers, write a function 
indexEqualsValueSearch that returns the lowest index i for which 
arr[i] == i. Return -1 if there is no such index. Analyze the time 
and space complexities of your solution and explain its correctness.
'''
import f_timer
import random

def index_equals_value_search(arr):
  for i in range(len(arr)):
    if i == arr[i]:
      return i
  return -1

def index_equals_value_search2(arr):
  # compare middle to middle index
  # if index greater go down, vice versa
  
  lowest_found = len(arr)
  left = 0
  right = len(arr)-1

  while(left <= right):
    i = (left+right)//2
    if arr[i] >= i :
      if arr[i] == i and i < lowest_found:
        lowest_found = i
      right = i - 1
    elif arr[i] < i:
      left = i + 1

  return lowest_found if lowest_found < len(arr) else -1


def gen_sorted_rand_arr(minVal, maxVal, maxLength):

  true_max_length = min(maxVal - minVal, maxLength)
  length = random.randint(0,true_max_length)
  nums = sorted(random.sample(range(minVal, maxVal), length))
  return [nums]

time,res = f_timer.get_func_time_and_res([index_equals_value_search, index_equals_value_search2], gen_sorted_rand_arr, [-500,10005,10000],1000)

valid = [0 if a == -1 else 1 for a in res]
print(sum(valid)/len(valid))
