list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def Function(list,i = 0):
    try:
        print(list[i*3])
        i+=1
        rec(list,i)
    except IndexError:
        return
rec(list)