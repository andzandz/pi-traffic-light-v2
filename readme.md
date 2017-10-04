# Andy/SoSLUG's Wifi Traffic Light Demo

Hello! This is a simple, Python-powered, smartphone/tablet/laptop-controlled Raspberry Pi traffic light project.

It makes use of Flask, a micro web framework, to get a web server up and running with Python quickly. Normally this would be used to just return web pages to a web browser. This project combines Flask with the Python GPIO library.

Any questions? Contact me: 

![email](https://raw.githubusercontent.com/andzandz/pi-traffic-light-v2/master/contact.png)

This is an improved/simplified version of a previous attempt at the same concept (https://github.com/andzandz/soslug-web-udp-controlled-pi-traffic-light) which used Python, JavaScript and PHP. This project has no JavaScript or PHP(!), and is simpler.

When set up and running correctly, browse to the IP address of the Pi and you should see a web page, with some links to change the colour of the LEDs.

I'm using a 4tronix PiStop connected to BOARD pins 6, 8, 10 and 12(see www.pinout.xyz) - with the Gnd pin on pin 6. At around £3, these don't seem too expensive for use in small projects like this. 

Or you can wire up LEDs on a breadboard to the correct pins - there are a few different tutorials for this, such as this one: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

Connect your Pi to the internet, open a terminal and download the project with `git clone`: (do not type the $)

```
$ git clone https://github.com/andzandz/pi-traffic-light-v2
```

You will need to install the flask python module, with pip3 (pip, for python 3). On your Pi, open a terminal and run:

```
$ sudo pip3 install flask
```

Make a note of your Pi's IP address by running

```
$ ifconfig
```

and you should see some lines beginning with "inet addr", such as

```
        inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
```

The first set of 4 numbers is the IP address, in this case 192.168.1.1. Make a note of this.

Then, you should be able to run the web server

```
$ sh pi-traffic-light-v2/run-server.sh
```

Once it says "Running on http://0.0.0.0:80", you should be able to browse to the Pi's IP address on any device connected to the same network as your Pi.

Now go explore the code and see how it works. I've commented it fairly thoroughly. The whole thing is only 86 lines of Python, including empty lines and comments.

It is also possible to set up the Pi to crete its own WiFi hotspot so anyone nearby can connect. I feel this is a little beyond beginner level, but feel free to ask about how I did it.

----------

This project was built by Andy K, STEM Ambassador and Chair of SoSLUG, local Southend computing/technology club.
