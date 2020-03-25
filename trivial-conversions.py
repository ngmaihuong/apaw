# Minutes to hours
while True:
    prompt = input("Minutes to hours [please type 1] or Hours to minutes [please type 2], please [q to quit]: ")
    if prompt == 'q':
        break
    while prompt == "1":
        value = input("Minutes to hours, please [q to quit]: ")
        if value == 'q':
            break
        number = int(value)
        print(number, "minutes is", number / 60, "hours")
    while prompt == "2":
        value = input("Hours to minutes, please [q to quit]: ")
        if value == 'q':
            break
        number = int(value)
        print(number, "hours is", number * 60, "minutes")

# Fahrenheit to Celcius
while True:
    prompt = input("F to C [please type 1] or C to F [please type 2], please [q to quit]: ")
    if prompt == 'q':
        break
    while prompt == "1":
        value = input("Degree Fahrenheit to Celcius, please [q to quit]: ")
        if value == 'q':
            break
        number = int(value)
        print(number, "degree Fahrenheit is", (number - 32) * (5/9), "degree Celcius")
    while prompt == "2":
        value = input("Degree Celcius to Fahrenheit, please [q to quit]: ")
        if value == 'q':
            break
        number = int(value)
        print(number, "degree Celcius is", number / (5/9) + 32, "degree Fahrenheit")
#How do I continue with my conversion choice without having to specify the prompt after each conversion? SOLVED- Change "if" to "while"
