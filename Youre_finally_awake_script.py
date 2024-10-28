"""
Script Name: Youre_finally_awake_script.py

Description:
This script plays random song from folder pointer by user at windows boot.
It reads configuration settings from a file named script_data.txt and adjusts the volume based on those settings.
The script can optionally increment the volume at regular intervals.

Configuration Settings:
- alarm_clock_enabled: If set, the script will not activate during boot if the current hour is greater than the stop_hour.
- stop_hour: The latest hour at which the script will execute.
- music_folder_path: The directory containing MP3 files.
- initial_volume: The volume level set at the beginning of the script.
- volume_increment_enabled: If enabled, the script will increment the volume by a specified amount at regular intervals.
- volume_increment_interval_seconds: The duration in seconds between volume increments.

Example:
alarm_clock_enabled=1
stop_hour=20
initial_volume=30
volume_increment_enabled=1
volume_increment_interval_seconds=5
music_folder_path=C:\\Users\\My\\myMusic (use double backslash '\\')

Author: JMamej

Date: 28.10.2024

Version: 0.2
"""

import os, time, random, sys
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from mutagen.mp3 import MP3
from datetime import datetime

# Initialize variables
alarm_clock_enabled = None
stop_hour = None
music_folder_path = None
initial_volume = None
volume_increment_enabled = None
volume_increment_interval_seconds = None

error_sleep_time = 10
max_volume_level = 0.99
volume_increment_step = 0.01

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read data from script_data.txt with error handling
try:
    with open('script_data.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')

            if key.strip() == 'alarm_clock_enabled':
                alarm_clock_enabled = int(value.strip())

            elif key.strip() == 'stop_hour':
                stop_hour = int(value.strip())

            elif key.strip() == 'music_folder_path':
                music_folder_path = value.strip()

            elif key.strip() == 'initial_volume':
                initial_volume = int(value.strip())

            elif key.strip() == 'volume_increment_enabled':
                volume_increment_enabled = int(value.strip())

            elif key.strip() == 'volume_increment_interval_seconds':
                volume_increment_interval_seconds = int(value.strip())

except FileNotFoundError:
    print("Error: script_Data.txt file not found.")
    time.sleep(error_sleep_time)
    sys.exit()

except ValueError as e:
    print("Error: Invalid value in script_Data.txt:", e)
    time.sleep(error_sleep_time)
    sys.exit()


# Define the variables
variables = {
    'alarm_clock_enabled': alarm_clock_enabled,
    'stop_hour': stop_hour,
    'music_folder_path': music_folder_path,
    'initial_volume': initial_volume,
    'volume_increment_enabled': volume_increment_enabled,
    'volume_increment_interval_seconds': volume_increment_interval_seconds
}

# Iterate over the variables and check for None values
for key, value in variables.items():
    if value is None:
        #print if the variable is None
        print(f"Error: '{key}' value not found in script_Data.txt.")
        time.sleep(error_sleep_time)
        sys.exit()
        
# If alarm_clock_enabled=1, script will run until chosen hour (stop_hour)
if alarm_clock_enabled:
    time_now = datetime.now()
    if (int(time_now.strftime("%H")) > stop_hour):
        sys.exit()


# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


# Check and open directory (music_folder_path)
if os.path.exists(music_folder_path):
    dir_list = os.listdir(music_folder_path)
    
    # Choose a random song from the directory
    random_item = random.choice(dir_list)
    song = os.path.join(music_folder_path, random_item)
else:
    print("Folder path does not exist.")
    time.sleep(error_sleep_time)
    sys.exit()

# Choosing sleep time each volume increase if increase_volume_option=1
if volume_increment_enabled: 
    sleep_time = volume_increment_interval_seconds

print("Now playing:", random_item, "\n\nEnjoy.")

# Play MP3 with initial volume setting
os.startfile(song)
volume.SetMasterVolumeLevelScalar((initial_volume/100), None)

# Infinite loop incrementing windows volume by 1 every sleep_time seconds untill it reaches 100
while volume.GetMasterVolumeLevelScalar() < max_volume_level:
    volume.SetMasterVolumeLevelScalar(volume.GetMasterVolumeLevelScalar() + volume_increment_step, None)
    time.sleep(sleep_time)
