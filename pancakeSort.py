'''
Given an array of integers arr:

    Write a function flip(arr, k) that reverses the order of the first k 
    elements in the array arr.
    Write a function pancakeSort(arr) that sorts and returns the input array. 
    You are allowed to use only the function flip you wrote in the first step 
    in order to make changes in the array.

Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a 
plate with a spatula, where you can only use the spatula to flip some of the 
top pancakes in the plate. To read more about the problem, see the Pancake 
Sorting Wikipedia page.
'''
def pancake_sort(arr):
  for i in range(len(arr)):
    
    #find largest remaining element
    max_loc = 0
    for j in range(len(arr) - i):
      if arr[j] > arr[max_loc]:
        max_loc = j
        
    #move it to the front
    flip(arr, max_loc)
    
    #move it in front of the greater maxes
    flip(arr, len(arr)-(i+1))
    
  return arr
    
        
        
      
  
def flip(arr, k):
  for i in range(k//2 + 1):
    arr[i],arr[k-i] = arr[k-i],arr[i]
  return arr



