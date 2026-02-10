def max_sum_no_consequtive(arr):
  n = len(arr)

  if n == 0:
    return 0
  elif n == 1:
    return max(0, arr[0])

  include = max(0, arr[0])
  exclude = 0

  for i in range(1, n):
    new_include = arr[i] + exclude
    new_exclude = max(include, exclude)

    include, exclude = new_include, new_exclude

  return max(include, exclude)

# example usage
arr = [3, 4, 7, 10]
print("The maximum sum with no consequtive elements: ", max_sum_no_consequtive(arr))