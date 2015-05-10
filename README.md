AirQuality
===========================================
        Get data from http://113.108.142.147:20035/emcpublish/ and parse them, finally save the data into the database

#Component

        Use python-wcfbin to convert wcf binary message files to xml files
        please see https://github.com/bluec0re/python-wcfbin

#Usage
        If you read all my code and construct the database like mine, then you can execute the total.py file directly.

        python3 total.py

        Please change your own config.ini. I offer a sample as config_demo.ini

        if you don't want to store the data, please read the code in air3.py and total.py.

