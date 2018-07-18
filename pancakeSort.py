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



