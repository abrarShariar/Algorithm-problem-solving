
def find_averages_of_subarrays(K, arr):
    # initialize the result array
    result = []
    current_sum = 0
    window_start = 0
    avg = 0
    
    # loop over the array list
    for window_end in range(len(arr)):
        if window_end < K:
            current_sum += arr[window_end]
        else:
            avg = round(current_sum/K, 1)
            result.append(avg)
            current_sum -= arr[window_start]
            current_sum += arr[window_end]
            window_start += 1

    result.append(round(current_sum/K, 1))
    return result

def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
