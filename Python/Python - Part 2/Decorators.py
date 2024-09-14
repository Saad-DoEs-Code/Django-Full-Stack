def new_decorator(func):
    print("Inside new_decorator")

    def wrap_func():
        print("BEFORE EXECUTING FUNC()")
        func()
        print("AFTER EXECUTING FUNC()")

    return wrap_func


# Wrap function will be copeid to "func_needs_decorator" with reference to "func_needs_decorator" definition

# func_needs_decorator = new_decorator(func_needs_decorator)
# This can be done as follows
@new_decorator
def func_needs_decorator():
    print("I need decorater")

func_needs_decorator()


