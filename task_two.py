

def file_getter_gen(*args):
    """
    Generator which return file-by-file line-by-line order
    :param args: name of files
    :return: file-by-file line-by-line order of args
    """
    s = [open(x, 'r') for x in args]
    while s:
        for i in s:
            temp = i.readline()
            if not temp:
                i.close()
                del s[s.index(i)]
                break
            yield temp
