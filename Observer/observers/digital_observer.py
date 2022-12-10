from observers.observer import Observer
import time

class DigitalObserver(Observer):
    def update(self, generator):
        print(f"DigitalObserver: {generator.getNumber()}")
        interval = 0.1
        time.sleep(interval)