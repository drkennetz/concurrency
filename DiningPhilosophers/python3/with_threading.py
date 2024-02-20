import random
import threading
import time
from typing import List

""" This solution avoids deadlock by never waiting for a chopstick while having one in hand.
If a philosopher acquires one chopstick but can't acquire the second, they will release
the first before waiting to acquire another (which then becomes the first acquired).
"""


class DiningPhilosopher(threading.Thread):
    """An example class to show the dining philosopher's problem in python"""

    def __init__(
        self,
        name: str,
        left_stick: threading.Lock,
        right_stick: threading.Lock,
        stop_event: threading.Event,
    ):
        super().__init__()
        self.name = name
        self.left_stick = left_stick
        self.right_stick = right_stick
        self.stop_event = stop_event

    def run(self):
        """override for thread.run which starts when threads start"""
        while not self.stop_event.is_set():
            self.think()
            self.eat()

    def think(self):
        print(f"{self.name} is daydreaming about food.")
        time.sleep(random.uniform(3, 13))

    def eat(self):
        """Dining philosophers eat. This is the main focus of the algorithm,
        and the place that simulates the philosopher's attempt to acquire
        both chopsticks for eating.
        """
        stick1, stick2 = self.left_stick, self.right_stick

        while not self.stop_event.is_set():
            with stick1:
                if stick2.acquire(blocking=False):
                    break
            stick2, stick1 = stick1, stick2
        else:
            return

        self.start_eating()
        stick2.release()

    def start_eating(self):
        print(f"{self.name} starts eating because they acquired 2 sticks!")
        time.sleep(random.uniform(1, 10))
        print(f"{self.name} finishes eating and leaves to think.")


def main():
    sticks: List[threading.Lock] = [threading.Lock() for _ in range(5)]
    philosopher_names = ["Becky", "Neka", "Jim", "Miriam", "JC"]
    stop_event = threading.Event()
    philosophers = [
        DiningPhilosopher(name, sticks[i % 5], sticks[(i + 1) % 5], stop_event)
        for i, name in enumerate(philosopher_names)
    ]
    random.seed(500000)
    for p in philosophers:
        p.start()
    time.sleep(100)
    stop_event.set()  # Stop threads
    print("The restaurant kicked the philosophers out.")


if __name__ == "__main__":
    main()
