import random
import time


class TaskSolution:
    @staticmethod
    def print_numbers_up_to_5():
        numbers = list(range(1, 8))
        for n in numbers:
            if n == 5:
                break
            print(n)

    @staticmethod
    def print_words():
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)


class Rostics:
    @staticmethod
    def check_load():
        i = 10
        while i > 0:
            load = random.randint(0, 100)
            print(f"Load: {load}%", "WARNING!" if load > 85 else "OK")
            time.sleep(0.2)
            i -= 1
