cd /home/ubuntu/code/github/AirQuality
mkdir log
python3 main_city.py >> ./log/log_city.dat
python3 main_station.py >> ./log/log_station.dat
