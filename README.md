# Raspberry Pi Home Automation

A home automation system built on Raspberry Pi that controls appliances remotely and sends email alerts through Gmail.

## Features
- Control appliances (lights, fans) using a relay module
- Sensor-based automation (motion / temperature / light)
- Automatic email alerts via Gmail SMTP
- Secure login using Google 2-Step Verification and an App Password

## Hardware
- Raspberry Pi
- Relay module
- Sensors (PIR / DHT11 / LDR)
- Jumper wires and power supply

## Software
- Raspberry Pi OS
- Python 3
- RPi.GPIO
- smtplib (email alerts)

## How it works
1. Sensors detect motion, light or temperature changes.
2. The Raspberry Pi processes the input and switches the relay.
3. An email alert is sent to the owner through Gmail SMTP.

## Email Setup
1. Enable 2-Step Verification in your Google Account.
2. Go to Security → App passwords → Mail → Other → Generate.
3. Store the 16-character password in a config file. Do not upload it to GitHub.

## Setup
1. Connect the relay and sensors to the GPIO pins.
2. Add your email and app password in `config.py`.
3. Run: `python3 main.py`

## Author
Sanjana