import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "It's Time to Drink Water",
            message = "Hi Akash, Let's be Hydrated. Mentain the required water intake!",
            app_name = "Drink Water",
            app_icon = "./Pani.ico",
            timeout = 10
        )
        time.sleep(60)
