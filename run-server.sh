# This bash script is just a terminal command so you don't have to type it out in full each time
# --host=0.0.0.0: Run on all interfaces (allow other devices to browse)
# --port=80: The default port number that web browsers use (HTTP), so instead of typing 192.168.1.1:80 into
# a browser you can just use 192.168.1.1
sudo FLASK_APP=/home/pi/wifi_traffic_light/server.py flask run --host=0.0.0.0 --port=80
