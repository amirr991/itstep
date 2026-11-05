def log_action(function):
    def wrapper(*args, **kwargs):
        print("Начало выполнения функции")
        result = function(*args, **kwargs)
        print("Функция успешно завершена")
        return result

    return wrapper


@log_action
def greeting(name):
    return f"Привет, {name}!"


print(greeting("имя"))