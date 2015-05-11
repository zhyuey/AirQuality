import xml.etree.ElementTree
import re
import sys
import datetime
import configparser
import sqlite3

print('#################################################################')
if len(sys.argv) < 2:
    print("Please specify the input file")
    sys.exit()
else:
    filename = sys.argv[1]

create_city_info_table = False
create_city_tables = False
update_items = True

file_object = open(filename, 'r')
try:
    all_the_text=file_object.read()
finally:
    file_object.close()

print(datetime.datetime.now())

all_the_text = re.sub("&mdash;", " ", all_the_text)


root = xml.etree.ElementTree.fromstring(all_the_text)

result = root.getchildren()[0].getchildren()[1]
cnt = int(root.getchildren()[0].getchildren()[0].text)
print(cnt)

##################################################################
# Parse the Configuration file and Connect to Mysql Server


conn = sqlite3.connect('./air_city_data.db')
cur = conn.cursor()


newcnt = 0
oldcnt = 0
##################################################################
for node in result.getchildren():
    child = node.getchildren()

    AQI = child[0].text
    Area = child[1].text
    CO = child[2].text
    CityCode = child[3].text
    Id = child[4].text
    Measure = child[5].text
    NO2 = child[6].text
    O3 = child[7].text
    PM10 = child[9].text
    PM2_5 = child[10].text
    PrimaryPollutant = child[11].text
    Quality = child[12].text
    SO2 = child[13].text
    TimePoint = child[14].text
    if create_city_info_table:
        sql = "insert into CITY(ID, AREA, CITYCODE) VALUES('%s', '%s', '%s')" % (Id, Area, CityCode)
        print(sql)
        cur.execute(sql)
        conn.commit()

    if create_city_tables:
        sql = "create table %s (AQI Int(10) default -1, CO float default -1, NO2 Int(10) default -1,O3 Int(10) default -1,  PM10 Int(10) default -1, PM2_5 Int(10) default -1, PrimaryPollutant Varchar(50), SO2 Int(10) default -1, TimePoint datetime Primary Key)" %  (Area)
        #sql = "drop table %s" % (StationCode)
        print(sql)
        cur.execute(sql)
        conn.commit()

    if update_items:
        sql = "insert into %s (AQI, CO, NO2, O3,  PM10,  PM2_5, PrimaryPollutant, SO2, TimePoint) values ('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s')" % (Area, AQI, CO, NO2, O3, PM10, PM2_5, PrimaryPollutant, SO2, TimePoint)
        #print(sql)
        try:
            cur.execute(sql)
        except:
            oldcnt = oldcnt + 1
            continue
        conn.commit()
        newcnt = newcnt + 1



print('New Items: ', newcnt)
print('Old Items: ', oldcnt)

print('TimePoint: ', TimePoint)
cur.close()
conn.close()
print('#################################################################')
