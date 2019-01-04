
table_card = input()
is_valid = False

hand_cards = input().strip().split(' ')
for card in hand_cards:
    if card[0] == table_card[0] or table_card[1] == card[1]:
        is_valid = True
        break

if is_valid:
    print("YES")
else:
    print("NO")
