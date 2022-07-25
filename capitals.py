capitals = {'Turkey': 'Ankara',
            'Azerbaijan': 'Baku',
            'Russia': 'Moscow',
            'USA': 'Washington DC',
            'Greece': 'Atina'}

while 1:
    key = input("Which city do you want to know: ")
    if not key.istitle():
        if not key.capitalize() in capitals:
            print("ERROR")
        else:
            print("correcting first letter...")
            print(capitals.get(key.capitalize()))
    elif key.istitle():
        print("searching...")
        print(capitals.get(key))

    while 1:
        user_input = input("Press 1 to enter new city, press 2 to pass: ")
        if user_input == "2":
            break
        elif user_input == "1":
            country_name = input("Enter country name: ")
            capital_name = input("Enter capital name: ")
            capitals.update({country_name.capitalize(): capital_name.capitalize()})
            # capitals[country_name.capitalize()] = capital_name.capitalize()
        else:
            print("Please re enter value")

