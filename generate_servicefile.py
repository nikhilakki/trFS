# Copyright (C) 2021 Nikhil Akki
# 
# This file is part of trFS (Tiny RESTful File Server).
# 
# trFS (Tiny RESTful File Server) is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# trFS (Tiny RESTful File Server) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with trFS (Tiny RESTful File Server).  If not, see <http://www.gnu.org/licenses/>.
import subprocess
import os

def bash_cmd(cmd: str):
    result = subprocess.check_output(cmd, shell=True)
    return result.decode("utf-8").strip("\n")


python_env = bash_cmd("which python")
pwd = bash_cmd("pwd")
user = bash_cmd("echo $USER")
service_file = f"""[Unit]
Description = tiny restful File Server
After = network.target
 
[Service]
Type = simple
ExecStart = {python_env} {pwd}/serve.py
User = {user}
Group = {user}
Restart = on-failure # Restart when there are errors
SyslogIdentifier = {pwd}/service.log
RestartSec = 5
TimeoutStartSec = infinity

[Install]
WantedBy = multi-user.target # Make it accessible to other users"""

service_file_path = os.path.join(pwd, "fileserver.service")
with open(service_file_path, "w") as f:
    f.write(service_file)

print(f"file written to path - {service_file_path}")