from collections import deque

input_file = list(map(int, open('input1', 'r').read().strip().split('\n')))
input_file0=[-3,0,2]
input_file=[
2115,
3713,
4975,
-7020,
-3949,
0,
-603,
-5596,
9212,
1244,
-559,
]
position_list = deque([(value, index) for index, value in enumerate(input_file)])
print(position_list)
print()
for i, num in enumerate(input_file):
    current_index = position_list.index((num, i))
    position_list.remove((num, i))
    position_list.rotate(-num)
    position_list.insert(current_index, (num, i))
    print(position_list)

final_list = list(map(lambda x: x[0], position_list))
zero_index = final_list.index(0)
print(zero_index)
print(final_list)
print(len(final_list))
print(sum(final_list[(zero_index+1000*i) % len(input_file)] for i in [1, 2, 3]))
