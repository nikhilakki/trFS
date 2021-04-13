## trFS a.k.a Tiny RESTful File Server

![trFS-screenshot](https://user-images.githubusercontent.com/17634231/114540004-ad24b180-9c72-11eb-9c46-b402df73791b.png)

* I made this in a couple of hours to access PDFs from RPI3 server to kindle (using the default browser which comes with it).
This app is very basic and serves the purpose it was built for :)

* Feel free to customize it as per your liking! 

### Limitations -

- This is by no means a secure application (intended for trusted local network, I use it on my local wifi)
- Read only mode (files can only be accessed/read)
- If you want more features you are better off using samba server (link [1](https://magpi.raspberrypi.org/articles/samba-file-server), [2](https://ubuntu.com/tutorials/install-and-configure-samba#1-overview), [3](http://www.linuxandubuntu.com/home/what-is-samba-server-and-how-to-setup-samba-server-in-ubuntu-linux) for reference)


### Requirements -

- Linux OS
- Python 3.7+
- pipenv (for virtualenv & dependencies installation)

### How to install

```bash
git clone https://github.com/nikhilakki/trFS.git
cd trFS
python3 -m pip install pipenv # if pipenv is not installed on your system
python3 -m pipenv install # to install all python depedencies for this app

pipenv run python generate_servicefile.py # generate systemd service file
sudo ./register.sh # registers & initiates the process with systemd - sudo will be required, please check the script before running
./status.sh # shows whether service has started successfully 
```

### How to run

create .env file with following content (customize it as requried)
```
PORT=8080 # configurable 
SHAREPATH="/home/pi/share/files" # change this according to your setup
```
then run the following commands on bash

```bash
export work_dir=$(pwd)
./register.sh
./status.sh
```

*Tested on Raspbian Linux for Rpi3*

> License - GPLv3

> Author - Nikhil Akki

> Version - 0.1.0