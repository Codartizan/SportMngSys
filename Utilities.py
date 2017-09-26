
def tuple_to_str(tar_tuple):
    """
    Convert the element of tuple to string
    :param tar_tuple: Target tuple element
    :return: New string
    """
    res = ''
    for a in tar_tuple:
        if type(a) is type(tar_tuple):
            res += tuple_to_str(a)
        else:
            res += str(a)
    return res
