import time
import smtplib
from email.message import EmailMessage

import RPi.GPIO as GPIO
import config  # holds your email and app password

RELAY_PIN = 17
PIR_PIN = 4
LDR_PIN = 27  # digital LDR module: HIGH = dark

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.output(RELAY_PIN, GPIO.LOW)


def send_email(subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = config.EMAIL
    msg["To"] = config.EMAIL
    msg.set_content(body)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(config.EMAIL, config.APP_PASSWORD)
            server.send_message(msg)
        print("Email sent:", subject)
    except Exception as e:
        print("Email failed:", e)


try:
    print("Home automation running... Ctrl+C to stop")
    last_alert = 0
    while True:
        motion = GPIO.input(PIR_PIN)
        dark = GPIO.input(LDR_PIN)

        # Light turns on only when it is dark AND motion is detected
        if motion and dark:
            GPIO.output(RELAY_PIN, GPIO.HIGH)
        else:
            GPIO.output(RELAY_PIN, GPIO.LOW)

        # Email alert on motion (at most once per 60 seconds)
        if motion and time.time() - last_alert > 60:
            send_email("Home Automation Alert", "Motion detected!")
            last_alert = time.time()

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopped")
finally:
    GPIO.cleanup()
