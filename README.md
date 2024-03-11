# Project Description:

This repository contains a Python script designed to play random music files from a specified directory upon system boot, providing a pleasant wake-up experience. The script reads configuration settings from a file (script_data.txt) to customize its behavior, including setting the alarm time, initial volume level, and options for volume incrementation. With its simple setup and customizable settings, this script offers a seamless way to start your day with your favorite tunes.

# Features:

Plays random music files upon system boot.

Customizable alarm time and volume settings.

Option to increment volume gradually over time.

Easy configuration via script_data.txt file.


# Usage:

Ensure script_data.txt is correctly configured.

Configuration Settings:
- alarm_clock_enabled: If set, the script will not activate during boot if the current hour is greater than the stop_hour.
- stop_hour: The latest hour at which the script will execute.
- music_folder_path: The directory containing MP3 files.
- initial_volume: The volume level set at the beginning of the script.
- volume_increment_enabled: If enabled, the script will increment the volume by a specified amount at regular intervals.
- volume_increment_interval_seconds: The duration in seconds between volume increments.

Run the script to activate the wake-up music functionality.

![image](https://github.com/jmamej/Python-Wake-Up-Music/assets/57408600/17e3534d-3c49-461a-b4ba-d145a9b791b7)


# Windows setup

To set up the script, paste the .exe and .txt files into the Autostart folder. You can access this folder by pressing Win + R and typing "shell:startup".

# Waking up PC

The process may vary depending on your system's BIOS. Here are examples for different BIOS systems:

![image](https://github.com/jmamej/Python-Wake-Up-Music/assets/57408600/1f64e506-05ec-4d05-a0e9-b99414fb0841)

![image](https://github.com/jmamej/Python-Wake-Up-Music/assets/57408600/b56f0a29-a4b1-4c9e-b9b6-cdabb87aac2a)

![image](https://github.com/jmamej/Python-Wake-Up-Music/assets/57408600/73ab4a84-07e0-4c1e-8dc4-8a70ea2c714b)


These images demonstrate autostart configurations on different BIOS systems.
