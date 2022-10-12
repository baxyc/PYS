# Реализуйте калькулятор



actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

for_test = "8 + 2 * 4 + ( 6 + ( 2 - 3 * 7 + ( 77 - 11 ) ) * 2 )"

def find_proiroty(numbers: list):
    new_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] == '(':
            if '(' in numbers[i + 1:]:
                numbers = numbers[:i + 1] + find_proiroty(numbers[i + 1:])
            g =  numbers.index(')', i)
            new_numbers.append(numbers[i + 1: g])
            i = g
        else:
            new_numbers.append(numbers[i])
        i+=1
    return new_numbers
changed_list = find_proiroty(for_test.split())
print(find_proiroty(for_test.split()))

def calc (numbers: list):
    for i, num in enumerate(numbers):
        if isinstance(num, list):
            numbers[i] = calc(num)
    new_list = [x for x, sym in enumerate(numbers) if sym in '*/']
    while new_list:
        k = new_list[0]
        a, b, c = numbers[k - 1: k + 2]
        numbers.insert(k - 1, actions[b](a, c))
        del numbers[k: k + 3]
        new_list = [x for x, sym in enumerate(numbers) if sym in '*/']
    while len(numbers) > 1:
        a, b, c = numbers[:3]
        del numbers[:3]
        numbers.insert(0, actions[b](a, c))
    return numbers[0]
print(calc(changed_list))





