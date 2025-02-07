# tests for function call

from chattool import Chat, generate_json_schema
import json

# schema of functions
functions = [
{
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA",
            },
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location", "unit"],
    },
}]

weatherinfo =  {
    "location": "Boston, MA",
    "temperature": "72",
    "forecast": ["sunny", "windy"],
    "unit":"celsius"
}
name2func = {
    'get_current_weather': lambda *kargs, **kwargs: weatherinfo
}

def test_function_call():
    chat = Chat("What's the weather like in Boston?")
    resp = chat.getresponse(functions=functions, function_call='auto')
    # TODO: wrap the response
    if resp.finish_reason == 'function_call':
        # test response from chat api
        parainfo = chat[-1]['function_call']
        func_name, func_args = parainfo['name'], json.loads(parainfo['arguments'])
        assert func_name == 'get_current_weather'
        assert 'location' in func_args and 'unit' in func_args
        # continue the chat
        chat.function(weatherinfo, func_name)
        chat.getresponse()
        # chat.save("testweather.json")
        chat.print_log()
    else:
        print("No function call found.")
        assert True

def test_function_call2():
    chat = Chat("What's the weather like in Boston?")
    chat.functions, chat.function_call = functions, 'auto'
    chat.name2func = name2func
    chat.autoresponse(max_requests=2)
    chat.print_log()

# generate docstring from functions
def add(a: int, b: int) -> int:
    """
    This function adds two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def mult(a:int, b:int) -> int:
    """
    This function multiplies two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b

def test_generate_docstring():
    functions = [generate_json_schema(add)]
    chat = Chat("find the sum of 784359345 and 345345345")
    chat.functions, chat.function_call = functions, 'auto'
    chat.name2func = {'add': add}
    chat.autoresponse(max_requests=2)
    chat.print_log()
    # use the setfuncs method
    chat = Chat("find the value of 124842 * 3423424")
    chat.setfuncs([add, mult])
    chat.autoresponse()
    chat.print_log()
