import logging
import time

# Налаштування логування
logging.basicConfig(filename='geometric_progression.log', level=logging.INFO)


# Декоратор для логування часу початку та закінчення подій
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{func.__name__} виконано за {end_time - start_time} секунд")
        return result
    return wrapper


# Клас ітератора для геометричної прогресії
class GeometricProgressionIterator:
    def __init__(self, start, multiplier):
        self.start = start
        self.multiplier = multiplier
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current *= self.multiplier
        return result


# Функція-генератор для геометричної прогресії
def geometric_progression_generator(start, multiplier):
    current = start
    while True:
        yield current
        current *= multiplier


# Функція для обчислення суми перших n елементів геометричної прогресії
@log_execution_time
def sum_of_geometric_progression(n, start=1, multiplier=3):
    progression = GeometricProgressionIterator(start, multiplier)
    # Або: progression = geometric_progression_generator(start, multiplier)
    total_sum = sum(next(progression) for _ in range(n))
    return total_sum


if __name__ == "__main__":
    # Визначення суми перших 10, 100, 1000 елементів
    for n in [10, 100, 1000]:
        total_sum = sum_of_geometric_progression(n)
        print(f"Сума перших {n} елементів геометричної прогресії: {total_sum}")
