import heapq
from collections import defaultdict
from re import search

f = 'single.txt'
# f = '17_test.in'

D = open(f).read().split('\n\n')

R = []
for line in D[0].splitlines():
    rval = line.split(':')[1]
    R.append(int(rval))

P = []
for p in D[1].split(':')[1].split(','):
    P.append(int(p))

print(R)
print(P)


def operand_value(op, r):
    vals = [0, 1, 2, 3, r[0], r[1], r[2]]
    assert 0 <= op < len(vals)
    return vals[op]


def execbc(P, R):
    out = []
    ip = 0
    while True:
        # print(ip, R)
        if ip >= len(P) - 1:
            break
        opc = P[ip]
        op = P[ip + 1]
        if opc == 0:  # adv
            R[0] = R[0] >> operand_value(op, R)
            ip += 2
            continue
        if opc == 1:  # bxl
            R[1] = R[1] ^ op
            ip += 2
            continue
        if opc == 2:  # bst
            R[1] = operand_value(op, R) & 7
            ip += 2
            continue
        if opc == 3:  # jnz
            if R[0] == 0:
                ip += 2
            else:
                ip = op
            continue
        if opc == 4:  # bxc
            R[1] = R[1] ^ R[2]
            ip += 2
            continue
        if opc == 5:
            val = operand_value(op, R) & 7
            out.append(val)
            ip += 2
            continue
        if opc == 6:  # bdv
            R[1] = R[0] >> operand_value(op, R)
            ip += 2
            continue
        if opc == 7:  # cdv
            R[2] = R[0] >> operand_value(op, R)
            ip += 2
            continue
    return out


out = execbc(P, R)
print("Part 1: ",','.join(map(str, out)))


# inA = (1 << 47)
# while inA < (1 << 48):
#     # reset
#     R[1] = R[2] = 0
#     inA += 1
#     R[0] = inA
#     out = execbc(P, R)
#     print(out)
#     if out != P:
#         continue
#     print(inA)


def go(a, p, l):
    if l == len(p) + 1:
        return a

    cand = []
    for w in range(8):
        out = execbc(p, [(a << 3) | w, 0, 0])
        p_suff = p[len(p) - l:]
        if out != p_suff:
            continue
        na = go((a << 3) | w, p, l + 1)
        if na:
            cand.append(na)

    if cand:
        return min(cand)
    return None


R[0] = R[1] = R[2] = 0
a = go(0, P, 1)
print("Part 2:",a)

R[0] = R[1] = R[2] = 0
R[0] = a
     