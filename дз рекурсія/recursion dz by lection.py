def RecursionListSum(el):
    if isinstance(el, list):
        sum = 0
        for item in el:
            sum = sum + RecursionListSum(item)

        return sum
    else:
        return el
print(RecursionListSum([1,[2,[3],[1,2]],4]))

