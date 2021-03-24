x = 4
y = 11
print('x = 4')
print('y = 11')
print("------------------")

print('binary', x, 'adalah =' ,format(x, '08b'))
print('binary', y, 'adalah =' ,format(y, '08b'))

# 4 | 11
print('_____________ 4 | 11 _____________')
z = x | y
print('binary', z, 'adalah =' ,format(z, '08b'))

# 4 >> 11
print('_____________ 4 >> 11 ____________')
p = x >> y
print('binary', p, 'adalah =' ,format(p, '08b'))

# 4 ^ 11
print('_____________ 4 ^ 11 _______________')
q = x ^ y
print('binary', q, 'adalah =' ,format(q, '08b'))

# ~4
print('______________ ~4 _______________')
r = ~x
print('binary', r, 'adalah =' ,format(r, '08b'))

# 11 & 4
print('______________ 11 & 4 ____________')
s = x & y
print('binary', s, 'adalah =' ,format(s, '08b'))