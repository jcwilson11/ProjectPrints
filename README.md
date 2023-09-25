# ProjectPrints
New Repo for my first coding project

## Project Description
The purpose of this project is the using a raspberry pi and usb camera to display and monitor my 3d printer when away from home in order to ensure that everything is running smoothly. The project is still in the early stages of development and is not yet ready for use. The primary language is going to python 3.10.
If possible, I would like to be able to use the raspberry pi to look for specific conditions and then send a text message to my phone if something is wrong. I would also like to be able to use the raspberry pi to control the printer remotely, but that is a secondary goal.

## Helpful Commands
- `ssh -X jcwil@raspberrypi` - ssh into the raspberry pi
- `exit` - exit the ssh connection

- `sudo apt-get update` - updates the raspberry pi
- `sudo apt-get upgrade` - upgrades the raspberry pi
- `sudo apt-get install python3-pip` - installs pip3
- `sudo raspi-config` - opens the raspberry pi configuration menu
- `sudo shutdown -h now` - shuts down the raspberry pi - now can be replaced with a time in minutes
- `vcgencmd get_camera` - checks if the camera is connected
- `lsusb`- to check if the camera is recognized at the USB level.
- `raspistill -o test.jpg` - takes a picture with the camera and saves it as test.jpg
- `sudo reboot` - reboots the raspberry pi
- `ifconfig` - shows the ip address of the raspberry pi
- `sudo systemctl status vncserver-x11-serviced` - shows the status of the vnc server
- `sudo systemctl start vncserver-x11-serviced` - starts the vnc server

- `tightvncserver` - starts the vnc server
- `tightvncserver -kill :1` - kills the vnc server
- open vnc viewer and type in the ip address of the raspberry pi

- `python3 server.py` - runs the server.py file
- `ls -l server.py` - shows the permissions of the server.py file and time of last edit

## Project Status
7.24.23 - Day 1
- camera py and server py created with no compiling errors. Hopefully with the use of python libraries like flask and opencv, I will be able to create a server that can be accessed from any device on the same network as the raspberry pi. The server will be able to display the camera feed and allow for remote control of the printer. The server will also be able to send text messages to my phone if something goes wrong with the printer.
- In order to start testing, I need to actually get a raspberry pi. I have ordered one and it should arrive in a few days. 

7.29.23 - Day 2
- all parts aquired
- got the raspberry pi setup using a hedless system and ssh
- working on sharing the python files between my computer and the raspberry pi

7.30.23 - Day 3
- tested the camera and it was able to take a picture, trying to set up a live feed
- server.py is able to run on the raspberry pi and display a live feed from the camera
- able to view virtual desktop of raspberry pi using vnc viewer
- able to add git repository to raspberry pi

8.1.23 - Day 4
- able to run server.py on raspberry pi and access it from my computer on an html page
- objectives: 
    - add a button to the html page that will take a picture and save it to the raspberry pi
    - make the cam feed smoother
    - add authentication to the html page

8.2.23 - Day 5
- added a login page to the html page. login works, but vid feed does not work
- login page works and leads to vid feed
- added a full screen screen, but it works for the whole page, not the video
- trying to add buttons to zoom in/out

9.8.23 - Day 6
- took a break from the project for a while since I was on vacation with family
- still working on the zoom in/out buttons
- camera is not being detected right now, trying to debug

9.11.23 - Day 7
- camera is working again
- expanding project to include a homepage with links to other pages
- one having my 3d prints, and another having my 3d printer viewer


