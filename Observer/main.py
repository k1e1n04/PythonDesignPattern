from observers.digital_observer import DigitalObserver
from observers.graph_observer import GraphObserver
from subjects.random_number_generator import RandomNumberGenerator

def start_main():
    generator = RandomNumberGenerator()
    observer1 = DigitalObserver()
    observer2 = GraphObserver()
    generator.addObserver(observer1)
    generator.addObserver(observer2)
    generator.execute()


if __name__ == "__main__":
    start_main()