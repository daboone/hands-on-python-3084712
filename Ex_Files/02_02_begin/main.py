greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

firstName = "Daniel"
lastName = "Lower"

intrupution = f"Hello {firstName}"

greet_format = "Hello {} {}"

formatted = greet_format.format(firstName, lastName)

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace('Daniel', 'Paul'))

