from observers.observer import Observer
import time

class GraphObserver(Observer):
    def update(self, generator):
        print(f"GraphObserver:",end="")
        count = generator.getNumber()
        for _ in range(count):
            print('*',end="")
        print("")
        interval = 0.1
        time.sleep(interval)