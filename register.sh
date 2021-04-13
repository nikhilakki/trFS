echo 'registering fileserver service as deamon process!'
sudo mv fileserver.service /lib/systemd/system/fileserver.service
sudo systemctl enable fileserver.service
echo 'starting fileserver deamon process...'
sudo systemctl start fileserver.service
echo 'complete!'