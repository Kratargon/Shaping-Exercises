def mergeList(first, second, t):
    if t == "append":
        newList = []
        for i in first:
            newList.append(i)
        for i in second:
            newList.append(i)
        return first
    if t == "alternate":
        newList = []
        for i in len(first) + len(second):
            if i % 2 == 0:
                newList.append(first[i//2])
            else:
                newList.append(second[i//2])
        return newList
    return "Error"