# Shoval Hadad

from functools import reduce
import time
import math


# Q1:

f = lambda x: x / 2 + 2
lst = list(map(f, range(0, 10001)))

# 1.2
def superSum(lst):
    return reduce(lambda x, y: x + y, lst)

# 1.3
def normalSum(lst):
    s = 0
    for i in lst:
        s += i
    return s

#if __name__ == "__main__":
t = time.time()
superSum(lst)
t = time.time() - t
print(t * 1000)

t = time.time()
normalSum(lst)
t = time.time() - t
print(t * 1000)

# 1.4
t = time.time()
sum(map(f, range(0, 10001)))
t = time.time() - t
print(t * 1000)



# Q2:

numbers = list(range(1, 1001))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))

# 2.1
b1 = lambda x: reduce( lambda a, b: a * b, even_numbers[:x] )
b2 = lambda x: f(x)

# 2.2
even_result = [b1(x) for x in range(1, len(even_numbers) + 1)]
odd_result = [b2(x) for x in odd_numbers]

# 2.3
#if __name__ == "__main__":
print(reduce(lambda x, y: x + y, even_result))
print(reduce(lambda x, y: x + y, odd_result))


# Q3:

# 3.a
def armstrong_is(n):
    if not isinstance(n, int) or n <= 0:
        return False
    k = len(str(n))
    return sum(
        map(lambda digit: int(digit) ** k, str(n))
    ) == n

# 3.b
def range_armstrong(n1, n2):
    return list(
        filter(armstrong_is, range(n1, n2 + 1))
    )

# 3.c
#if __name__ == "__main__":
def mainQ3():
    try:
        n = int(input("enter number:\n"))
        if n <= 0:
            print("input invalid")
        else:
            print(range_armstrong(1, n))
    except ValueError:
        print("input invalid")


# Q4:

def dates(date, count, step):
    return list(
        map(lambda x: date + x * step, range(count))
    )


# Q5:

# 5.a
def power_f(n):
    return lambda x: x ** n

# 5.b
def power_map(n):
    return map(power_f, range(n))

#if __name__ == "__main__":
def mainQ5():
    n = int(input("Enter number of powers:\n"))
    result = power_map(n)
    print(type(result))
    base = int(input("Enter base:\n"))
    print(tuple(f(base) for f in result))

# 5.c
def taylor(x, n):
    powers = power_map(n + 1)
    return sum(
        map(
            lambda item:
            item[1](x) / math.factorial(item[0]),
            enumerate(powers)
        )
    )


# Q6:

def task_manager():
    tasks = {}

    def add_task(task, status="incomplete"):
        tasks[task] = status

    def get_tasks():
        return tasks

    def complete_task(task):
        if task in tasks:
            tasks[task] = "complete"

    return {
        "add_task": add_task,
        "get_tasks": get_tasks,
        "complete_task": complete_task
    }
#if __name__ == "__main__":
def mainQ6():
    manager = task_manager()
    manager["add_task"]("Write email")
    manager["add_task"]("Shopping", "in progress")
    manager["add_task"]("Homework")
    print(manager["get_tasks"]())
    manager["complete_task"]("Write email")
    print(manager["get_tasks"]())


# Q7:

# 7.a
def clean_spaces(text):
    return text.strip()

def capitalize_text(text):
    return text.title()

def add_stars(text):
    return "***" + text + "***"

# 7.b
def create_pipeline():
    return lambda x: x

def add_to_pipeline(pipeline_fn, new_fn):
    return lambda x: new_fn(pipeline_fn(x))

# 7.c
#if __name__ == "__main__":
def mainQ7():
    pipeline = create_pipeline()
    pipeline = add_to_pipeline( pipeline, clean_spaces )
    pipeline = add_to_pipeline( pipeline, capitalize_text )
    pipeline = add_to_pipeline( pipeline, add_stars )
    text = input("enter text:\n")
    if not text.strip():
        print("input invalid")
    else:
        print(pipeline(text))