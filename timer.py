from datetime import datetime, timedelta
import time
def timer():
    start_time = datetime.now()
    s = start_time.strftime("%H:%M")
    come_back = start_time + timedelta(seconds=7800)
    c = come_back.strftime("%H:%M")
    print("Finished transactions at:",s)
    print("Check back at:", c)
    time.sleep(1950)
    print("32.5 total minutes have passed")
    print("97.5 minutes remain")
    time.sleep(1950)
    print("65 total minutes have passed")
    print("65 minutes remain")
    time.sleep(1950)
    print("97.5 total minutes have passed")
    print("32.5 minutes remain")
    time.sleep(1950)
    print("Wait complete, beginning bot again..")