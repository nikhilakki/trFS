## trFS a.k.a Tiny RESTful File Server

* I made this in a couple of hours to access PDFs from RPI3 server to kindle (using the default browser which comes with it).
This app is very basic and serves the purpose it was built for :)

* Feel free to customize it as per your liking! 

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
```

### How to run

create .env file with following content (customize it as requried)
```
PORT=80
SHAREPATH="${work_dir}/files"
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