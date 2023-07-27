import operator as op

input_file = open('input0', 'r').read().strip().split('\n')
# input_file = open('input/input_test.txt', 'r').read().strip().split('\n')
monkey_dict = {}

for line in input_file:
    monkey_to_answer = line.split(': ')
    monkey_dict[monkey_to_answer[0]] = monkey_to_answer[1]


def search_monkeys(monkey, number):
    binary = {'*': op.mul, '+': op.add, '-': op.sub, '/': op.truediv}
    monkey_answer = monkey_dict[monkey].split()
    if monkey == 'humn':
        return number
    elif len(monkey_answer) == 1:
        return int(monkey_answer[0])
    else:
        return binary[monkey_answer[1]](search_monkeys(monkey_answer[0], number),
                                        search_monkeys(monkey_answer[2], number))


def equality_test(number):
    monkey_split = monkey_dict['root'].split()
    return search_monkeys(monkey_split[0], number) - search_monkeys(monkey_split[2], number)


def check_increasing():
    return equality_test(100) < equality_test(200)


def binary_search(best_upper, best_lower, increasing):
    average = (best_upper + best_lower)//2
    equality = equality_test((best_upper + best_lower)//2)
    print(best_upper, best_lower, average, equality)
    if equality == 0:
        return average
    else:
        if equality > 0 and increasing or equality < 0 and not increasing:
            return binary_search(average, best_lower, increasing)
        else:
            return binary_search(best_upper, average, increasing)


print(binary_search(10**16, 0, check_increasing()))
