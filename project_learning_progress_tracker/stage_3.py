
# create Student class using the given template.
# add format checks to the class
# https://realpython.com/python-class-constructor/
class MyClass:
    def __init__(self, param1, param2):
        # Check if param1 and param2 follow some rules
        if not self.validate_param1(param1):
            raise ValueError("param1 does not follow the rules")
        if not self.validate_param2(param2):
            raise ValueError("param2 does not follow the rules")

        # If all checks pass, set the instance variables
        self.param1 = param1
        self.param2 = param2

    def validate_param1(self, param1):
        # Add your validation logic for param1 here
        return param1 >= 0  # Example rule: param1 must be non-negative

    def validate_param2(self, param2):
        # Add your validation logic for param2 here
        return isinstance(param2, str) and len(param2) <= 10  # Example rule: param2 must be a string of length at most 10


# Usage
try:
    obj = MyClass(5, "hello")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Object created successfully")