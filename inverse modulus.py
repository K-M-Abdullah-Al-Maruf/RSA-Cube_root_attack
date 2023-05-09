inp = input("Enter: ").split(" mod ")
divider = int(inp[1])
inp = inp[0].split("^")
print(inp)
divisor, power = int(inp[0]), int(inp[1])
print("g r1 r2 r  t1 t2 t")
if power < 0:
    divisor %= divider
    r1 = divider
    r2 = divisor
    t1 = 0
    t2 = 1
# print(g, r1, "", r2, "", r, " ", t1, "", t2, "", t)
while True:
    g = r1 // r2
    r = r1 % r2
    # print(r)
    if r == 0:
        print(g, r1, "", r2, "", r, " ", t1, "", t2, "", t)
        if (t2 < 0):
            print("mod =", (divider + t2))
        else:
            print("mod =", (t2))
        break
    else:
        t = t1 - t2 * g
        t1 = t2
        t2 = t
        r1 = r2
        r2 = r
        print(g, r1, "", r2, "", r, " ", t1, "", t2, "", t)
