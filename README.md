AirQuality
===========================================
        Get data from http://113.108.142.147:20035/emcpublish/ and parse them,
        finally save the data into the database

#Component

		Use python-wcfbin to convert wcf binary message files to xml files
		please see https://github.com/bluec0re/python-wcfbin

		Use Sqlite3 to store data

#Usage
        If you have read all my code and construct the database like mine, 
        then you can execute the total.py file directly.

```
	python3 main_city.py
	python3 main_station.py
```



