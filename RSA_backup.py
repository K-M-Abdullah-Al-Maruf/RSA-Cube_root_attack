import math


def inverse_mod_calc(divisor, divider):
    divisor %= divider
    r1 = divider
    r2 = divisor
    t1 = 0
    t2 = 1
    while True:
        g = r1 // r2
        r = r1 % r2
        if r == 0:
            if t2 < 0:
                return divider + t2
            else:
                return t2
            break
        else:
            t = t1 - t2 * g
            t1 = t2
            t2 = t
            r1 = r2
            r2 = r


p, q, c, n = [3,5,13], [11,7,19], [], []
m = int(input("Enter the value of M = "))

# for i in range(6):
#     if i % 2 == 0:
#         p.append(int(input("Enter P" + str((i // 2) + 1) + ": ")))
#     else:
#         q.append(int(input("Enter q" + str((i // 2) + 1) + ": ")))

for i in range(len(p)):
    n.append(p[i] * q[i])

for i in range(3):
    c.append(m**3 % n[i])

for i in range(len(p)):
    print(f'Enter p{i}:', p[i])

for i in range(len(q)):
    print(f'Enter q{i}:', q[i])

for i in range(len(c)):
    print(f'Enter C{i}:', c[i])

x = 0
for i in range(3):
    x += (c[i] * n[(i + 1) % 3] * n[(i + 2) % 3] * inverse_mod_calc(n[(i + 1) % 3] * n[(i + 2) % 3], n[i]))


x = x % (n[0] * n[1] * n[2])
M = math.ceil(x ** (1 / 3))
print("\nM =", M)
