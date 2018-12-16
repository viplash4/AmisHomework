size = int(input("size of list "))
UserList = [int(input("Enter element ")) for i in range(0,size)]


def reverse(s):
    if (len(s) < 2):
        return s
    else:
        mid = len(s)//2
        return (reverse(s[mid:]) + reverse(s[:mid]))
print(reverse(UserList))
