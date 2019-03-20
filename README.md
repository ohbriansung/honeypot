# honeypot

## References

1. https://github.com/internetwache/SSH-Honeypot

# ssh-pot2

1. sudo apt-get install ssmtp 
2. sudo apt-get install mailutils
3. sudo nano /etc/ssmtp.conf
4. Include this info
root=postmaster
mailhub=smtp.gmail.com:587
hostname=-raspberrypi
AuthUser=gmailname@gmail.com
AuthPass=gmailpassword
FromLineOverride=YES
UseSTARTTLS=YES
5. sudo apt-get install mpack
6. Send a file: 
mpack -s "Subject" /home/pi/file.txt gmailname@gmail.com
7. Run the script logrecorder.sh
./logrecorder.sh &


