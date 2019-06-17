# total_items = int(input())
# org_item_dict = {}
# for i in range(total_items):
#     el = input()
#     org_item_dict[el] = '0'
#
#
# # print(org_item_dict)
# total_items = int(input())
# org_item_list = list(org_item_dict)
# for i in range(total_items):
#     price = float(input())
#     org_item_dict[org_item_list[i]] = price
#
#
# # print(org_item_dict)
# alex_count = int(input())
# alex_dict = {}
# for i in range(alex_count):
#     el = input()
#     alex_dict[el] = '0'
#
# count_fault = 0
# alex_count = int(input())
# alex_list = list(alex_dict)
# for i in range(alex_count):
#     num = float(input())
#     alex_dict[alex_list[i]] = num
#     if org_item_dict[alex_list[i]] != num:
#         count_fault += 1
#
# print(count_fault)


for i in range(len(items)):
    alex_price = prices[i]
