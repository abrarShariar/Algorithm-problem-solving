def two_sum(nums, goal):
  left_index = 0
  right_index = len(nums) - 1
  
  while left_index < right_index:
    sum = nums[left_index] + nums[right_index]
    if sum == goal:
      return [left_index, right_index]
    elif sum < goal:
      left_index += 1
    else:
      right_index -= 1

  return []