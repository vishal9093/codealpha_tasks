def Vishal(message):
    message = message.lower().strip()

    if "introduce yourself" in message or "introduction" in message:
         return "Hello! I am Vishal a basic Python chatbot created by Vishal Yadav."

    if "your age" in message or "how old are you" in message:
        return "I am a chatbot, so I don't have a human age."

    elif "where do you live" in message or "your location" in message:
        return "I live inside this Python program!"

    elif "favourite language" in message or "What is your favourite language" in message:
        return "Python is my favourite programming language!"

    elif "guido van rossum" in message or "who is guido van rossum" in message:
        return "Guido van Rossum created Python. Python was first released in 1991."

    elif "features of python" in message or "what are the features of python" in message:
        return "Python is easy to learn, readable, interpreted, and supports multiple programming styles."

    elif "data types" in message or "data type" in message or "what are the data types" in message:
        return "Python data types include int, float, str, bool, list, tuple, set and dict."

    elif "variable" in message or "what is a variable" in message:
        return "A variable stores a value. Example: name = 'Vishal'"

    elif "types of loop" in message or "what are the types of loop" in message:
        return "Python has two main loop types: for loops and while loops."

    elif "if else" in message or "conditional statement" in message:
        return "If-else statements help a program make decisions based on conditions."

    elif "list" in message or "what is a list" in message:
        return "A list stores multiple items. Example: fruits = ['apple', 'mango', 'banana']"

    elif "tuple" in message or "what is a tuple" in message:
        return "A tuple is an ordered collection that cannot be changed after creation."

    elif "dictionary" in message or "dict" in message or "what is a dictionary" in message:
        return "A dictionary stores information as key-value pairs."

    elif "function" in message or "what is a function" in message:
        return "A function is a reusable block of code defined using the def keyword."

    elif "oops" in message or "object oriented programming" in message or "what is oops" in message:
        return "OOP stands for Object-Oriented Programming. It uses classes and objects."

    elif "interpreter" in message or "what is an interpreter" in message:
        return "An interpreter executes program instructions. Python commonly runs through an interpreter."

    elif "artificial intelligence" in message or "what is ai" in message:
        return "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."

    elif "machine learning" in message or "what is machine learning" in message:
        return "Machine learning allows computers to learn patterns from data."

    elif "database" in message:
        return "A database is an organized collection of information that can be stored and retrieved."

    elif "html" in message or "what is html" in message:
        return "HTML stands for HyperText Markup Language. It structures web pages."

    elif "css" in message or "what is css" in message:
        return "CSS stands for Cascading Style Sheets. It styles web pages."

    elif "java" in message or "Define is java" in message:
        return "Java is a popular programming language used for applications and software development."

    elif "career" in message or "how to build a career in programming" in message:
        return "Build strong fundamentals, practise projects, and improve your communication skills."

    elif "job" in message or "how to get a job in programming" in message:
        return "Learn relevant skills, build projects, prepare your resume, and practise interviews."

    elif "motivate me" in message or "motivation" in message or "what is motivation" in message:
        return "Believe in yourself! Every expert was once a beginner. Keep practising."

    elif "favourite colour" in message or "favorite color" in message or "what is your favourite colour" in message:
        return "I don't have personal preferences, but blue is a nice colour!"

    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day. See you again!"
print("------------------------------------------")
print("             BASIC CHATBOT")
print("------------------------------------------")
print("Hello! I am Vishal (Chatbot).")
print("I can answer some basic questions.")
print("Type 'help' to know what I can do.")
print("Type 'bye' to exit the chatbot.")
print("------------------------------------------")

while True:

    message = input("\nYou: ")

    # Check for empty input
    if message.strip() == "":
        print("Bot: Please type something.")
        continue

    # Get chatbot response
    answer = Vishal(message)

    print("Bot:", answer)

    # Exit chatbot
    if "bye" in message.lower() or "goodbye" in message.lower():
        break

print("\n------------------------------------------")
print("       Chatbot session ended.")
print("       Thank you for using SimpleBot!")
print("        Have a nice day           ")
print("        Namaste             ")
print("------------------------------------------")