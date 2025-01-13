import threading
import time

class DiningPhilosophers:
    def __init__(self, n_philosophers):
        self.n_philosophers = n_philosophers
        self.forks = [threading.Condition() for _ in range(n_philosophers)]

    def pick_forks(self, philosopher_id):
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.n_philosophers

        with self.forks[left_fork]:
            with self.forks[right_fork]:
                print(f"Philosopher {philosopher_id} is eating. ")
                time.sleep(2)

    def dine(self, philosopher_id):
        for _ in range(3):
            print(f"Philosopher {philosopher_id} is thinking. ")
            time.sleep(2)
            print(f"Philosopher {philosopher_id} is hungry. ")
            self.pick_forks(philosopher_id)
        print(f"Philosopher {philosopher_id} is done.")

n = int(input("Enter number of philosophers: "))
philosophers = []

dining_table = DiningPhilosophers(n)

for i in range(n):
    philosopher = threading.Thread(target = dining_table.dine, args=(i,))
    philosophers.append(philosopher)
    philosopher.start()

for philosopher in philosophers:
    philosopher.join()

print("Dining complete.")