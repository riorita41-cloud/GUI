_stack = []  # список Python — хранит элементы стека

def init():
    global _stack
    _stack = []

# push добавляет элемент на вершину стека.
def push(name, age):
    global _stack #функция будет менять _stack

    # Проверка данных
    if not name or not name.strip():
        return False
    if age < 0:
        return False
    # Добавляем элемент на вершину стека (конец стека)
    _stack.append((name.strip(), age))
    return True

# Удаление верхних элементов из стека
def pop_element():
    global _stack

    if len(_stack) == 0:# Проверка на пустой стек
        return False

    _stack.pop()  # удаляем последний элемент (вершину)
    return True

#Посмотреть верхний элемент( без удаления).
def peek():
    global _stack

    if len(_stack) == 0: # стек пуст
        return ("__EMPTY__", -1)

    return _stack[-1]  # последний элемент = вершина

#Получить количество элементов в стеке
def size():
    global _stack
    return len(_stack)

def get_all(): #Получить все элементы стека
    global _stack

    # Возвращаем в обратном порядке: вершина  → основание
    return list(reversed(_stack))

def clear():#Очистить весь стек.
    global _stack

    count = len(_stack)
    _stack = []
    return count


def is_empty(): #Пуст ли стек.
    global _stack
    return len(_stack) == 0
