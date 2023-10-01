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