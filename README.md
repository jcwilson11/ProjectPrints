# **Project Prints**

## **Repository Overview**
This repository is dedicated to "Project Prints," a personal venture to create a remote monitoring system for a 3D printer using a Raspberry Pi and USB camera.

---

## **Project Description**
Aiming to monitor and control a 3D printer remotely, this project is in the early development stages. The core technology involves a Raspberry Pi and a USB camera, with Python 3.10 as the primary programming language. Current objectives include setting up the Raspberry Pi to detect specific conditions and send alerts via text message, and potentially controlling the printer remotely.

### **Development Tools and Commands**
- SSH, system updates, camera checks, and network configurations on Raspberry Pi.
- Python development, including running and editing server files.
- VNC server management for remote access.

---

## **Project Goals**
- **Primary Goal**: Implement a system to monitor the 3D printer using a Raspberry Pi and USB camera.
- **Secondary Goal**: Develop features for remote control of the printer and automated alerts.

---

*For more information or to contribute to this project, please feel free to contact me at [jcwilson2021@outlook.com](mailto:jcwilson2021@outlook.com) or via [LinkedIn](https://www.linkedin.com/in/joriswilson11/)**


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
