
def delta_encode(array):
    new_array = []
    new_array.append(array[0])
    for i in range(1, len(array)):
        new_val = array[i] - array[i-1]
        if not (-127 <= new_val <= 127):
            new_array.append(-128)
        new_array.append(new_val)

    return new_array

def main():
    array_cnt = 0
    array_cnt = int(input())
    array_i = 0
    array = []
    while array_i < array_cnt:
        array_item = int(input())
        array.append(array_item)
        array_i += 1


    res = delta_encode(array)
    print(res)

main()
