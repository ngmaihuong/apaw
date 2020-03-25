# Converting minutes to hours

while True:
    value = input("Minutes to hours, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    print(number, "minutes is", number / 60, "hours")
