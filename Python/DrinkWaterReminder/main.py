# For notification in python use external library search -> (notification in python)
# I am using this library :-   https://pypi.org/project/plyer/      -> also install this library
# This is for documentation:-  https://plyer.readthedocs.io/en/latest/

import time 
from plyer import notification

while True:
    print("Please sip some water !")
    notification.notify(
    title="💧 Time to Drink Water!",
    message="Stay hydrated. Take a sip now!",
    timeout=10,  # seconds
    app_name="Hydration Reminder"
)

    # time.sleep(3)       # Give time in second 
    time.sleep(60 * 60)        # Work in 1 hour of interval

# You need to also set the environment for dbus
