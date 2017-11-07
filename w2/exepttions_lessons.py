def f(x, y):
    try:
        return x / y
    # Use with e and args
    # except ZeroDivisionError as e :
    #     print(type(e))
    #     print(e)
    #     print(e.args)

    # use with tuple of exceptions
    except (ZeroDivisionError, TypeError):
        print("Some error here")



print(f(10,0))

def foo():
    pass


#===================================================
try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
#===================================================
try: foo()
except (ZeroDivisionError, AssertionError, ArithmeticError ) as e:
    if isinstance(e, ZeroDivisionError): print('ZeroDivisionError')
    elif isinstance(e, ArithmeticError): print('ArithmeticError')
    elif isinstance(e, AssertionError): print('AssertionError')
#===================================================
try: foo()
except (ZeroDivisionError, AssertionError) as e: print(str(type(e))[8:-2])
except ArithmeticError: print('ArithmeticError')


class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0:
            list.append(x)
        else:
            raise NonPositiveError

class NonPositiveError(ArithmeticError):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        super().append(x)



