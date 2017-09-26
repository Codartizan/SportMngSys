import pymysql
import Utilities
import random
import GroupingUtil
from logzero import logger  # Github page: https://github.com/metachris/logzero

# db = pymysql.connect(host='localhost', port=3306, user='root', passwd='tim1279', db='sportmngsys', charset='UTF8')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='sportmngsys', charset='UTF8')
cursor = db.cursor()

data = cur = cursor.execute('SELECT TEAM_NAME FROM TEAM;')

teamList = []

for i in cursor:
    iStr = Utilities.tuple_to_str(i)
    teamList.append(iStr)
    # print(iStr)

random.shuffle(teamList)

db.close()

group_count = 7
team_count = 5

result_ls = GroupingUtil.div_group(teamList, group_count, team_count)

print('Team Total count: ' + str(len(teamList)))
logger.debug('Team Total count: ' + str(len(teamList)))

k = 1

for i in result_ls:
    print('Group ' + str(k) + '|-- ' + str(i))
    logger.info(i)
    k = k + 1
