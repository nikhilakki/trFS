echo 'moving file to systemd location...'
sudo mv fileserver.service /lib/systemd/system/fileserver.service
echo 'restarting systemd deamon...'
systemctl daemon-reload
echo 'registering fileserver service as deamon process!'
systemctl enable fileserver.service
echo 'starting fileserver deamon process...'
systemctl start fileserver.service
echo 'complete!'