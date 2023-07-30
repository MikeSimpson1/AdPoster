#!/bin/bash
python3 home/mike/Desktop/Projects/CameraApplication.py
scp -r /home/mike/Desktop/Projects/Images Mike@192.168.11.5:Desktop/Projects/MarketplaceAdPoster
ssh 'mike@192.168.11.5' 'powershell schtasks /run /tn MarketplaceAdPoster'
