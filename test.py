import numpy as np

def Gen_zero_matrix(m,n):

    A=[[0 for i in range(m-1)] for i in range(n-1)]
    return A

def make_nd_list(dim,n,initial_value):
    if n == 1:
        return [initial_value for i in range(dim[n - 1])]
    else:
        return [make_nd_list(dim, n - 1, initial_value) for i in range(dim[n - 1])]

#def shape_nd_list(nd_list,depth):
#    for i in range(depth):
#        nd_shape.append(len(nd_list[n]))



x=[[2,5],[4,7,[3,5,5]],4]
print len(x)
print x[1]
print len(x[1])
print x[1][2]

dim=[2,3,4]
B=make_nd_list(dim,3,1)
print B
