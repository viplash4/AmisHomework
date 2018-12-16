size = int(input("size of list "))
UserList = [int(input("Enter element ")) for i in range(0,size)]

def Min(UserList):
    if len(UserList) ==1:
        return UserList[0]
    else:
        number = Min(UserList[1:])
        if number < UserList[0]:
            return number
        else:
            return UserList[0]

print(Min(UserList))
