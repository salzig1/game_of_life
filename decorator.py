def count_calls(func):
    def wrapper(*args, **kwargs):
        count_calls.call_count += 1
        return func(*args, **kwargs)
    count_calls.call_count = 0
    return wrapper