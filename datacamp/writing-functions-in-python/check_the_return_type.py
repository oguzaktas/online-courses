'''
Instructions
- Start by completing the returns_dict() decorator so that it raises an AssertionError 
if the return type of the decorated function is not a dictionary.
- Now complete the returns() decorator, which takes the expected return type as an argument.
'''

def returns(return_type):
  # Complete the returns() decorator
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      assert(type(result) == return_type)
      return result
    return wrapper
  return decorator
  
@returns(dict)
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')