l1 = [1,2,3,9,9,9]
l2 = [1,2,3,9]
n = max(len(l1),len(l2))
op = [0] * (n+1)
carry = 0
print(n)
for i in range(0,n):
    o1 = l1[i] if i < len(l1) else 0
    o2 = l2[i] if i < len(l2) else 0
    tot = o1 + o2 + carry
    op[i] = tot % 10
    carry = tot // 10
    print(op[i])
if carry > 0:
    op[n] = carry
if op[-1] == 0:
    op = op[:-1]
print(op)