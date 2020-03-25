# Minutes to hours

while True:
    value = input("Minutes to hours, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    print(number, "minutes is", number / 60, "hours")

# Fahrenheit to Celcius

while True:
    value = input("Degree Fahrenheit to Celcius, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    print(number, "degree Fahrenheit is", (number - 32) * (5/9), "degree Celcius")
    #How do I include a prompt to choose which side I want to convert?
