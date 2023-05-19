def calculate(input_str):
    stack = []
    tokens = input_str.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 / operand2)

    return stack.pop()

input_str = input()
result = calculate(input_str)
print(result)
