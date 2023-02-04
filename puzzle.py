def rekha(n,a,b,c):
    if n>0:
        rekha(n-1,a,c,b)
        if a:
            c.append(a.pop())
            rekha(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
rekha(len(a),a,b,c)
print("print after puzzle")
print(a,b,c)
