message = "This is the first program"
print(message)

message_1 = "changed the variable value"
print(message_1)

# "f-string"
formatted_message = f"The current value of the message is: {message}"
print(formatted_message)

#how to include apostrophe(single and double quotes) in the string
message_with_quotes = "It's a beautiful day"  #single quote
print(message_with_quotes)
#dor double quotes
message_with_quotes_double = 'He said, "Hello!"'  #double quote
print(message_with_quotes_double)

full_message = f'{message} and {message_1}'
print(full_message)
# adding the upper() and lower() inside the f-string
full_message = f'{message.upper()} and {message_1.lower()}'
print(full_message)

# Using title() method 
name = "john doe"
print(name.title())  # Capitalizes the first letter of each word

#for removing the spaces from the string we use the strip() method
name = "   Vikas   "
print(name.rstrip()) # removes spaces from right
print(name.lstrip()) # removes spaces from left
print(name.strip())  # removes spaces from both sides


# trying

name = "bharat kumar"
print(f"Hello, {name.title()} how are you?")

print(f"Hello, {name.upper()}")
print(f"Hello, {name.lower()}")
print(f"Hello, {name.title()}")


quote = "Life is not about waiting for the storm to pass but about learning to dance in the rain."
print(f'Vivian Greene once said, "{quote}"')

famous_person = "Vivian Greene"
message = f'{famous_person} once said, "{quote}"'
print(message)

name = "VIkas"
print('/t' + name.upper() + '/t')