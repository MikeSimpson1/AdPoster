#!/bin/bash
python3 home/mike/Desktop/Projects/RaspberryPi/CameraApplication.py
python3 home/mike/Desktop/Projects/RaspberryPi/ProcessImages.py
scp -r /home/mike/Desktop/Projects/Images Mike@192.168.11.10:Desktop/Projects/MarketplaceAdPoster
ssh 'mike@192.168.11.10' 'powershell schtasks /run /tn MarketplaceAdPoster'
