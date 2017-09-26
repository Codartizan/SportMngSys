import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='tim1279', db='sportmngsys', charset='UTF8')
cursor = db.cursor()

data = cur = cursor.execute('SELECT TEAM_NAME FROM TEAM;')


def tupletostr(tuple):
    res = ''
    for a in tuple:
        if type(a) is type(tuple):
            res += tupletostr(a)
        else:
            res += str(a)
    return res


for i in cursor:
    iStr = tupletostr(i)
    print(iStr)

db.close()