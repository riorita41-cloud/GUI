import ctypes  # для работы с DLL
import os  # для работы с папками и файлами

# Находим путь к DLL
dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DLL.dll")

dll = ctypes.CDLL(dll_path, use_last_error=True) # Эта строка открывает DLL и загружает её в память

dll.init_stack.restype = None  # тип возврата
dll.init_stack.argtypes = []  # типы аргументов

# описывают функцию push в DLL
dll.push.restype = None
dll.push.argtypes = [ctypes.c_wchar_p, ctypes.c_int]
# ctypes.c_wchar_p = "указатель на широкую строку"
# ctypes.c_int = "целое число"

# pop() — без аргументов
dll.pop.restype = None
dll.pop.argtypes = []

# peek_name() — возвращает строку
dll.peek_name.restype = ctypes.c_wchar_p
dll.peek_name.argtypes = []

# peek_age() — возвращает целое число
dll.peek_age.restype = ctypes.c_int
dll.peek_age.argtypes = []

# get_size() —  возвращает количество элементов в стеке
dll.get_size.restype = ctypes.c_int
dll.get_size.argtypes = []

# get_name_at(index)  возвращает строку
dll.get_name_at.restype = ctypes.c_wchar_p
dll.get_name_at.argtypes = [ctypes.c_int]

# get_age_at(index)  возвращает int
dll.get_age_at.restype = ctypes.c_int
dll.get_age_at.argtypes = [ctypes.c_int]

# clear_stack() — без аргументов
dll.clear_stack.restype = None
dll.clear_stack.argtypes = []

def init():
    dll.init_stack()

 #Функция проверяет: имя не пустое, возраст не отрицательный
def push(name: str, age: int) -> bool:
    if not name or not name.strip():
        return False  # пустое имя — ошибка
    if age < 0:
        return False  # отрицательный возраст — ошибка

    # Если все хорошо,вызываем C++ функцию push из DLL
    dll.push(name.strip(), age)
    return True


def pop_element() -> bool: # возвращаем True, если удалось удалить, и False, если стек был пуст.
    if dll.get_size() == 0:
        return False
    dll.pop()
    return True


def peek() -> tuple: #функция возвращает name, age.

    name = dll.peek_name()
    age = dll.peek_age()
    return (name, age)


def size() -> int:
    return dll.get_size()


def get_all() -> list: #список элементов

    elements = []
    count = dll.get_size()

    for i in range(count):
        name = dll.get_name_at(i)  # i=0 это вершина стека
        age = dll.get_age_at(i)
        elements.append((name, age))

    return elements


def clear() -> int:

    count = dll.get_size()
    dll.clear_stack()
    return count


def is_empty() -> bool:
    return dll.get_size() == 0

