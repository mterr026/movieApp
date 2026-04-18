from services import *

while True:
    print("Please choose an option below: ")
    print("(1) Add a movie to the list")
    print("(2) Show all movies in the list")
    print("(3) Show total spent")
    print("(4) Show expensive movies")
    print("(5) Find movie by name")
    print("(6) Delete movie")
    print("(7) Update movie price")
    print("(8) Average movie price")
    print("(9) Lowest movie prices")
    print("(10) Highest movie prices")
    print("(11) Save Movies")
    print("(12) Quit\n")

    choice = input()

    if choice == "1":
        add_movie()
    elif choice == "2":
        print(get_movies())
    elif choice == "3":
        print(get_total_amount())
    elif choice == "4":
        print(get_expensive_movies())
    elif choice == "5":
        print(get_movie_by_name())
    elif choice == "6":
        print(delete_movie())
    elif choice == "7":
        print(update_price())
    elif choice == "8":
        print(average_movie_price())
    elif choice == "9":
        print(lowest_price())
    elif choice == "10":
        print(highest_price())
    elif choice == "11":
        print(save_movies())
    elif choice == "12":
        print("Thank you, goodbye")
        break
    else:
        print("Please enter a valid option")

