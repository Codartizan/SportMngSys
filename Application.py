import pymysql
import Utilities

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='tim1279', db='sportmngsys', charset='UTF8')
cursor = db.cursor()

data = cur = cursor.execute('SELECT TEAM_NAME FROM TEAM;')

for i in cursor:
    iStr = Utilities.tupletostr(i)
    print(iStr)

db.close()