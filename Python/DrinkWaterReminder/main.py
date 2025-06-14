# For notification in python use external library search -> (notification in python)
# I am using this library :-   https://pypi.org/project/plyer/      -> also install this library
# This is for documentation:-  https://plyer.readthedocs.io/en/latest/

import time
from plyer import notification
from datetime import datetime

while True:
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f"[{current_time}] 💧 Please sip some water!")
    notification.notify(
        title=f"💧 Time to Drink Water! {current_time}",
        message="Stay hydrated. Take a sip now!",
        timeout=10,
        app_name="Hydration Reminder"
    )
    time.sleep(3)  # Use 60 * 60 for 1 hour
