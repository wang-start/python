def book(name):
    return "the name of my book is {0}".format(name)
def p_deco(func):
    def wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return wrapper

laoqi = p_deco(book)
py_book = laoqi("python大学实用教程")
print(py_book)
