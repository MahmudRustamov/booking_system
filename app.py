from datetime import datetime
import csv 


def my_decerator(func):
    def wrapper(*args, **kwargs):
        result =  func(*args, **kwargs)
        data = [datetime.now(), f"args: {args}", result]
        with open("log.csv", mode="a", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print("Data is saved")
        return result
    return wrapper


@my_decerator
def add(num1, num2):
    return num1 + num2

@my_decerator
def subtraction(num1, num2):
    return num1 - num2

print(add(15, 23))
print(subtraction(56, 35))