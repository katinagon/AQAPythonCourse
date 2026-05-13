class TaskSolution:
    @staticmethod
    def print_numbers_up_to_5():
        numbers = list(range(1, 8))
        for n in numbers:
            if n == 5:
                break
            print(n)
