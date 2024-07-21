li=[12,35,9,56,24]

def myfun(li):
    si = len(li)
    tem=li[0]
    li[0]=li[si-1]
    li[si-1]=tem

    return li
print(myfun(li))
