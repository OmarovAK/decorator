from datetime import datetime



def param_decor(file_path):
    def my_decor(func):
        def internal_function(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_path, mode='w', encoding='utf-8') as f:
                date = f'Время вызова функции: {datetime.now().time()}\n'
                f.writelines(date)
                name_function = f'Название функции - {func.__name__}\n'
                f.writelines(name_function)
                argums = f'Аргументы функции {func.__name__} - {args}\n'
                f.writelines(argums)
                f.writelines(result)
        return internal_function
    return my_decor
