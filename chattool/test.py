from marshmallow import Schema, fields
from docstring_parser import parse

def create_schema_from_docstring(func):
    # Parse the docstring
    docstring = parse(func.__doc__)

    # Create a dictionary to hold the fields
    field_dict = {}

    # Iterate over the parameters in the docstring
    for param in docstring.params:
        if param.type_name == "int":
            field_dict[param.arg_name] = fields.Int(description=param.description)
        elif param.type_name == "str":
            field_dict[param.arg_name] = fields.Str(description=param.description)
        # Continue for other types...

    # Create the schema
    schema = Schema.from_dict(field_dict)()

    return schema

# Your function
def calc_sum(a, b):
    """
    计算两个数的和

    Args:
        a (int): 第一个整数
        b (int): 第二个整数

    Returns:
        int: 两个数的和
    """
    return a + b

# Use the helper function to create the schema
calc_sum_schema = create_schema_from_docstring(calc_sum)

# Print the JSON schema
print(calc_sum_schema.schema)
