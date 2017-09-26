from logzero import logger

def div_group(ls, g, t):
    """
    Divide teams into groups base on given group count and team count
    :param ls: The list of team name
    :param g: Group count
    :param t: Team count for each group
    :return: A nested List
    """

    if not isinstance(ls, list) or not isinstance(g, int) or not isinstance(t, int):
        return []

    ls_return = []

    for i in range(0, g * t, t):
        ls_return.append((ls[i:i + t]))

    if g * t < len(ls):
        for i in ls_return:
            for k in i:
                ls.remove(k)

        for i in ls:
            print('Team ' + str(i) + ' has been removed')
            logger.debug('Team ' + str(i) + ' has been removed')

    return ls_return
