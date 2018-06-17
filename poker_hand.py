import re
from collections import Counter

while True:
    five_cards = input("Please enter 5 cards: ")
    if not re.match(r'((S|H|D|C)([2-9]|10|J|Q|K|A)){5}', five_cards):
        print("The string is invalid. Please try again")
    else:
        cards = [five_cards[x:x + 2] for x in range(0, 10, 2)]
        if(len(cards) != len(set(cards))):
            print("There is any card duplicate. Please try again")
        else:
            break

ranks = [card[1] for card in cards]
counter = Counter(ranks)
rs = set()
for i in counter:
    rs.add(counter[i])
if rs == {1, 4}:
    print("4C")
elif rs == {2, 3}:
    print("FH")
elif rs == {1, 1, 3}:
    print("3C")
elif rs == {1, 2, 2}:
    print("2P")
elif rs == {1, 1, 1, 2}:
    print("1P")
else:
    print("--")


