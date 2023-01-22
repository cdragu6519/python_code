# numbers that allow multiple solutions to a^3 + b^3

res = {}

for a in range(1, 501):
    for b in range(a, 501):
        n = a**3 + b**3
        if res.get(n) is None:
            res[n] = [(a, b)]
        else:
            res[n].append((a, b))
        # print(a, b, n)

print('===========================')
for k,v in res.items():
    if len(v) > 2:
        print(k, v)
