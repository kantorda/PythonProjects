# Four Function caluclator

input_tokens = input("Enter a math expression using '+-*/: ").split()

total = float(input_tokens[0])
next_op = ''

for tok in input_tokens[1:]:
    if tok in "+-*/":
        next_op = tok
    else:
        if next_op == '+':
            total += float(tok)
        elif next_op == '-':
            total -= float(tok)
        elif next_op == '*':
            total *= float(tok)
        else:
            total /= float(tok)

print(total)
