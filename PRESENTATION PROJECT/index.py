import mysql.connector
from time import sleep

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='gamemate',
         user='dbuser',
         password=' ',
         autocommit=True
         )

def selectedCountry(number):
    sql = "SELECT ID, name, capital, lang, currency, famous_for FROM country WHERE ID = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (number,))
    result = cursor.fetchall()
    for row in result:
        print(f"\nLet's learn about \033[4m{row[1]}\033[0m.\n"
              f"Capital of {row[1]} is \033[4m{row[2]}\033[0m.\n"
              f"Official language is \033[4m{row[3]}\033[0m.\n"
              f"Currency is \033[4m{row[4]}\033[0m.\n"
              f"{row[1]} is famous for \033[4m{row[5]}\033[0m.\n")
        print("The quiz starts in 15 sec ", end='\n', flush=True)
        # setting time
        sleep(15)
        print(" \n" * 40)
    print(f"So, we are talking about \033[4m{row[1]}\033[0m.")
    counter = 0
    user = input(str(f"What is the capital of \033[4m{row[1]}\033[0m? "))
    if user == str(row[2]):
        counter += 2
        #smiley
        print(f"Yes! It is a correct answer! \U0001f600 \nYou have got {counter} points\n ")
    else:
        print("Oops! That was wrong!\n")

    user = input(str(f"What is the language of \033[4m{row[1]}\033[0m? "))
    if user == str(row[3]):
        counter += 2
        print(f"Yes! It is a correct answer! \U0001f600 \nYou have got {counter} points\n ")
    else:
        print("Oops! That was wrong!\n")

    user = input(str(f"What is the currency of \033[4m{row[1]}\033[0m? "))
    if user == str(row[4]):
        counter += 2
        print(f"Yes! It is a correct answer! \U0001f600  \nYou have got {counter} points\n ")
    else:
        print("Oops! That was wrong!\n")

    user = input(str(f"What is \033[4m{row[1]}\033[0m famous for? "))
    if user == str(row[5]):
        counter += 2
        print(f"Yes! It is a correct answer! \U0001f600 \nYou have got {counter} points\n ")
    else:
        print("Oops! That was wrong!\n")
    # the total earned score will be printed at the end of the round
    print(f"You earned a total of {counter} points in this round.\n \n")


name = input("Please enter your name: ")
print(f"\nHello, {name}! Let's play a game COUNTRIES.\nIn this game you will learn"
      f" about countries we are from. "
      f"Then you will answer questions.\nAnd for every correct answer you get points.\n"
      f"                         LET'S START!\nBelow enter the number of the country you would like to know more about: \n \nNepal - 1"
      f"\nRussia - 2\nSri Lanka - 3\nPakistan - 4\nBangladesh - 5")

while True:
    number = int(input("Enter the number (or 0 to quit): "))
    if number == 0:
        break
    selectedCountry(number)
    print(
        f"{name}! Let's play again\nBelow enter the number of the country you would like to know more about: \n \nNepal - 1"
        f"\nRussia - 2\nSri Lanka - 3\nPakistan - 4\nBangladesh - 5\n")

print("\nBYE! BYE!")