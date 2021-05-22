# SOLVED
def validIPAddresses(string):
    if len(string) < 4:
        return []

    input_string_size = len(string)
    result_set = set()
    last_index_1 = 2
    # take the max possible first => go greedy
    while last_index_1 >= 0:
        first_set = string[:last_index_1+1]
        if not isValid(first_set):
            last_index_1 -= 1
            continue
        
        # genereate second set
        last_index_2 = last_index_1 + 3
        while last_index_2 > last_index_1 and last_index_2 < input_string_size:
            second_set = string[last_index_1 + 1:last_index_2 + 1]
            if not isValid(second_set):
                last_index_2 -= 1
                continue
            
            # generate the third set
            last_index_3 = last_index_2 + 3
            while last_index_3 > last_index_2:
                thrid_set = string[last_index_2 + 1: last_index_3 + 1]
                if not isValid(thrid_set):
                    last_index_3 -= 1
                    continue
                

                # generate the fourth set
                last_index_4 = input_string_size - 1
                while last_index_4 > last_index_3 and last_index_4 < input_string_size:
                    fourth_set = string[last_index_3 + 1: last_index_4 + 1]
                    if not isValid(fourth_set):
                        last_index_4 -= 1
                        continue
                
                    # combine the 3 sets => all valid
                    result_str = first_set + '.' + second_set + '.' + thrid_set + '.' + fourth_set
                    if len(result_str) == input_string_size + 3:
                        result_set.add(result_str)
                    last_index_4 -= 1
                last_index_3 -= 1

            last_index_2 -= 1

        last_index_1 -= 1

    return list(result_set)

    

def isValid(string):
    if len(string) == 0:
        return False
    if int(string) > 255 or int(string) < 0:
        return False
    elif string[0] == '0' and len(string) > 1: 
        return False

    return True


output_set = validIPAddresses('1921680')
for val in output_set:
    print(val)