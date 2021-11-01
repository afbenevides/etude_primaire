sudo apt update
sudo apt install espeak -y
mkdir /home/pi/espeak
cd /home/pi/espeak
wget https://raspberry-pi.fr/download/espeak/mbrola3.0.1h_armhf.deb -O mbrola.deb
sudo dpkg -i mbrola.deb
sudo apt install mbrola-fr1 -y