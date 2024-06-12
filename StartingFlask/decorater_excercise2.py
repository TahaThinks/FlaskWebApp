import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function_to_check):
    def time_calculation():
        start_time = time.time()
        function_to_check()
        end_time = time.time()
        print(f"for {function_to_check.__name__} Time Taken: {end_time-start_time}")
    return time_calculation


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        count = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        count = i * i



fast_function()
slow_function()