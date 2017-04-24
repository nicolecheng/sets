def union(A,B):
    l = [x for x in A]
    l.extend([y for y in B if y not in A])
    return l

#print union([1,2,3],[2,3,4])

def intersection(A,B):
    return [x for x in A if x in B]

#print intersection([1,2,3],[2,3,4])

def set_difference(A,B):
    return [x for x in A if x not in B]

#print set_difference([1,2,3],[2,3,4])
#print set_difference([2,3,4],[1,2,3])

def symmetric_difference(A,B):
    l = [x for x in A if x not in B]
    l.extend([y for y in B if y not in A])
    return l

#print symmetric_difference([1,2,3],[2,3,4])

def cartesian_product(A,B):
    return [[x,y] for x in A for y in B]

#print cartesian_product([1,2],["red","white"])
