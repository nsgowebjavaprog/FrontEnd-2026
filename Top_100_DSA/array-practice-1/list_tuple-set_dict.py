'''
list = [10,20,30]
print(list)
print(type(list))

tuple = (1,2,3,4)
print(tuple)
print(type(tuple))

set = {1,3,5,7,9,1}
print(set)
print(type(set))

# TUPLE --> Immutable

t = (1,2,3,4,4,'Tuple', True, 1000)
print(t)

print(t[0])
print(t.count(4))
print(t.index(4))
print(t[-1])  # 1000


# Tuple --> functions

t = (1,3,2,4)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
'''


# SET
'''
my_set = set()

s = {10, "Python", 3.14,10, True}

s = {1,2,3,4}

print(s)

# Methods

s.add(5)
print(s)

s.update([5,6,7])
print(s)

s.remove(7)
print(s)

s.discard(10)
print(s)

s.pop()
print(s)

s.clear()
print(s)

print(s)
dup_set = s.copy()
print(dup_set)
'''

# MATHS
'''
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# print(A.union(B))
# A.intersection(B)

print(A.difference(B))
print(A.symmetric_difference(B))


A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

print(A.issuperset(B))
'''
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))