import xml.etree.ElementTree
import re
import sys
import pymysql
import datetime
import configparser


print('#################################################################')
if len(sys.argv) < 2:
    print("Please specify the input file")
    sys.exit()
else:
    filename = sys.argv[1]

create_position_info_table = False
create_position_tables = False
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

config = configparser.ConfigParser()
config.read('config.ini')
sqlhost = config.get('mysql', 'sqlhost')
sqluser = config.get('mysql', 'sqluser')
sqlpasswd = config.get('mysql', 'sqlpasswd')
sqldb = config.get('mysql', 'sqldb')
sqlport = int(config.get('mysql', 'sqlport'))
sqlcharset = config.get('mysql', 'sqlcharset')


conn = pymysql.connect(host=sqlhost, user=sqluser, passwd=sqlpasswd, db=sqldb, port=sqlport, charset=sqlcharset)
cur = conn.cursor()


newcnt = 0
oldcnt = 0
##################################################################
for node in result.getchildren():
    child = node.getchildren()

    AQI = child[0].text
    Area = child[1].text
    CO = child[2].text
    CO_24h = child[3].text
    CityCode = child[4].text
    IsPublish = child[5].text
    Latitude = child[6].text
    Longitude = child[7].text
    Measure = child[8].text
    NO2 = child[9].text
    NO2_24h = child[10].text
    O3 = child[11].text
    O3_24h = child[12].text
    O3_8h = child[13].text
    O3_8h_24h = child[14].text

    OrderId = child[16].text
    PM10 = child[17].text
    PM10_24h = child[18].text
    PM2_5 = child[19].text
    PM2_5_24h = child[20].text
    PositionName = child[21].text
    PrimaryPollutant = child[22].text
    ProvinceId = child[23].text
    Quality = child[24].text
    SO2 = child[25].text
    SO2_24h = child[26].text
    StationCode = child[27].text
    TimePoint = child[28].text
    Unhealthful = child[29].text
    if create_position_info_table:
        sql = "insert into POSITION (ID, AREA, NAME, LATITUDE, LONGITUDE) values ('%s', '%s', '%s', '%f', '%f')" % (StationCode, Area, PositionName, float(Latitude), float(Longitude))
        print(sql)
        cur.execute(sql)
        conn.commit()

    if create_position_tables:
        sql = "create table %s (AQI Int(10) default -1, CO float default -1, CO_24H float default -1, NO2 Int(10) default -1, NO2_24H Int(10) default -1, O3 Int(10) default -1, O3_24H Int(10) default -1, O3_8H Int(10) default -1, O3_8H_24H Int(10) default -1, PM10 Int(10) default -1, PM10_24H Int(10) default -1, PM2_5 Int(10) default -1, PM2_5_24H Int(10) default -1, PrimaryPollutant Varchar(50), SO2 Int(10) default -1, SO2_24H Int(10) default -1, TimePoint datetime Primary Key) charset =utf8" %  (StationCode)
        #sql = "drop table %s" % (StationCode)
        #print(sql)
        cur.execute(sql)
        conn.commit()

    if update_items:
        sql = "insert into %s (AQI, CO, CO_24H, NO2, NO2_24H, O3, O3_24H, O3_8H, O3_8H_24H, PM10, PM10_24H, PM2_5, PM2_5_24H, PrimaryPollutant, SO2, SO2_24H, TimePoint) values ('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s','%s','%s')" % (StationCode, AQI, CO, CO_24h, NO2, NO2_24h, O3, O3_24h, O3_8h, O3_8h_24h, PM10, PM10_24h, PM2_5, PM2_5_24h, PrimaryPollutant, SO2, SO2_24h, TimePoint)
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
