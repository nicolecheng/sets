a = [1,2,3]
b = [2,3,4]
c = [3,5,8]

def union(A,B):
    for x in B:
        if not(x in A):
            A.append(x)
    return A

def intersection(A,B):
    R = []
    for x in B:
        if (x in A) and not (x in R):
            R.append(x)
    return R

def set_difference(A,B):
    R = []
    for x in A:
        if not(x in B):
            R.append(x)
    return R

def symmetric_difference(A,B):
    R = []
    for x in B:
        if not(x in A):
            R.append(x)
    for x in A:
        if not(x in B) and not(x in R):
            R.append(x)
    return R

def cartesian_product(A,B):
    R = []
    for x in A:
        for y in B:
            R.append([x,y])
    return R

"""
print union(a,b)

print intersection(a,b)
print intersection(a,c)
print intersection(c,b)

print set_difference(a,b)
print set_difference(b,a)

print symmetric_difference(a,b)
print symmetric_difference(b,c)

print cartesian_product([1,2],["red","white"])
"""
