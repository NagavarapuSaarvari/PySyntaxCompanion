import streamlit as st

# Dictionary mapping user inputs to Python syntax responses
syntax_responses = {
    "if condition": (
        "The syntax of if condition is\nif condition:\n    # Code block to execute if condition is True"
    ),
    "else if condition": (
        "The syntax of else if condition is\nif condition1:\n    # Code block to execute if condition1 is True\nelif condition2:\n    # Code block to execute if condition2 is True"
    ),
    "else condition": (
        "The syntax of else is\nif condition:\n    # Code block to execute if condition is True\nelse:\n    # Code block to execute if condition is False"
    ),
    "taking user input": (
        "The syntax for taking user input is\nuser_input = input('Enter something: ')"
    ),
    "for loop": (
        "The syntax of for loop is\nfor item in iterable:\n    # Code block to execute for each item in iterable"),
    "while loop": (
        "The syntax of while loop is\nwhile condition:\n    # Code block to execute while the condition is True"
    ),
    "lists": (
        "The syntax of list creation is\nmy_list = [1, 2, 3]"
    ),
    "tuples": (
        "The syntax of tuple creation is\nmy_tuple = (1, 2, 3)"
    ),
    "sets": (
        "The syntax of set creation is\nmy_set = {1, 2, 3}"
    ),
    "dictionary": (
        "The syntax of dictionary creation is\nmy_dict = {'key': 'value'}"
    ),
    "type conversion": (
        "The syntax for type conversion is\nconverted_variable = data_type(variable)"
    ),
    "string concatenation": (
        "The syntax for concatenating two strings is\nstring1 = 'Hello'\nstring2 = 'World'\nconcatenated_string = string1 + ' ' + string2"
    ),
    "functions": (
        "The syntax of function defition is\ndef my_function(parameters):\n    # Function code\n\n For calling the function:\nmy_function(arguments)"
    ),
    "files": (
        "Syntax to open a file\nwith open('filename.txt', 'r') as file:\n    content = file.read()"
    ),
    "classes": (
        "Syntax for declaring a class\nclass MyClass:\n     Class attributes"
    ),
    "constructors": (
        "The syntax for declaring a class and its constructor is\nclass MyClass:\n    def __init__(self, parameter):\n        self.attribute = parameter"
    ),
    "lambda function": (
        "function_name = lambda variable1,variable2: function defition"
    ),
}



def generate_python_syntax_response(user_input):
    #Generate a Python syntax response based on user input.
    response = "I'm sorry, I don't have information on that syntax. Please ask about a different Python syntax."

    # Check for keywords in the user input
    for keyword, syntax in syntax_responses.items():
        if keyword in user_input.lower():
            response = syntax
            break

    return response

#Website Design

#Page configuration
st.set_page_config(page_title="PySyntaxCompanion", layout="wide")
#Page tittle
st.markdown("<h1 style='text-align: center;'>Py Syntax Companion (PSC)</h1>", unsafe_allow_html=True)
st.subheader("Hi!How can I help you")
#User input
inp= st.text_input("You")


# Check if the user has entered something
if inp:
    # Generate Python syntax response
    syntax_response = generate_python_syntax_response(inp)
    
    # Display the response
    st.text_area("PySyntaxCompanion:", syntax_response)
