def filter_list_by_type(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) is list:
                filtered_result = [item for item in result if type(item) is not data_type]
                return filtered_result
            return result
        return wrapper
    return decorator

@filter_list_by_type(str)
def get_data():
    return ['wassermelone', 4235, 'birne', 45.132, 'banana', 1]

@filter_list_by_type(int)
def get_numbers():
    return [1, 2, 'drei', 3, 5.6]

@filter_list_by_type(float)
def get_mixed_data():
    return [12, 453, 'hallo', 61.8, 69]

print(get_data())
print(get_numbers())
print(get_mixed_data())
