import stack_stl

def init():
    stack_stl.init()

def push(name, age):
    return stack_stl.push(name, age)

def pop_element():
    if stack_stl.get_size() == 0:
        return False
    stack_stl.pop()
    return True

def peek():
    name = stack_stl.peek_name()
    age = stack_stl.peek_age()
    return (name, age)

def size():
    return stack_stl.get_size()

def get_all():
    return stack_stl.get_all()

def clear():
    stack_stl.clear_stack()

def is_empty():
    return stack_stl.get_size() == 0