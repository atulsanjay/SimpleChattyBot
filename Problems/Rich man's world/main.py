ir = int(input())

t = 0
while ir <= 700000:
    ir = ir + ((ir / 100) * 7.1)
    t += 1

print(t)