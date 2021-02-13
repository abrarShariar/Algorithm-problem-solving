# def findAllDuplicates(arr):
#     arr.sort()
#     count_dict = {}
#     result_list = []
#     for i in range(len(arr)):
#         count_dict[arr[i]] = count_dict.get(arr[i], 0) + 1

#     for key, value in count_dict.items():
#         if count_dict[key] > 1:
#             result_list.append(key)

#     return result_list


def fn(prices):
    # Write your code 
    answer_list = []

    if len(prices) <= 1:
        return prices

    for i in range(len(prices)):
        next_pointer = i + 1
        while next_pointer < len(prices):
            if prices[next_pointer] > prices[i]:
                answer_list.append(next_pointer - i)
                break
            next_pointer += 1
        answer_list.append(0)

    return answer_list
    