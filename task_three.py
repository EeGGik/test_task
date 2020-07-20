

def merge_gen(*item):
    """
    Merge multiple sorted inputs into a single sorted output.
    :param item:
    :return:
    """
    indexes = [ 0 if item[i] != None else None for i in range(len(item))]
    rez = [None for _ in range(len(indexes))]
    while rez != indexes:
        min = None
        for i in range(len(item)):
            if indexes[i] != None and (min == None or item[i][indexes[i]] < item[min[0]][min[1]]):
                min = (i, indexes[i])
        yield item[min[0]][min[1]]

        if indexes[min[0]]+1 < len(item[min[0]]):
            indexes[min[0]] += 1
        else:
            indexes[min[0]] = None
