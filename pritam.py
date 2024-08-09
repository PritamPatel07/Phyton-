# Asking the user to choose an option
a = input("Choose an option (Breakfast/Lunch/Dinner/Brunch): ")

# Displaying options based on user input
if a.capitalize() == "Breakfast":
    print("You chose Breakfast. Please choose a cuisine:")
    b = input("Enter 'South Indian' or 'North Indian': ")
    if b.capitalize() == "South Indian":
        print("You chose South Indian. Please choose a dish:")
        c = input("Enter 'Idli and Sambar', 'Dosa', 'Upma', or 'Pongal': ")
        if c.capitalize() == "Idli and Sambar":
            print("You chose Idli and Sambar.")
        elif c.capitalize() == "Dosa":
            print("You chose Dosa.")
        elif c.capitalize() == "Upma":
            print("You chose Upma.")
        elif c.capitalize() == "Pongal":
            print("You chose Pongal.")
        else:
            print("Invalid input. Please choose a valid dish.")
    elif b.capitalize() == "North Indian":
        print("You chose North Indian. Please choose a dish:")
        c = input("Enter 'Paratha with Curd and Pickle', 'Poha', 'Aloo Poori', or 'Chole Bhature': ")
        if c.capitalize() == "Paratha with Curd and Pickle":
            print("You chose Paratha with Curd and Pickle.")
        elif c.capitalize() == "Poha":
            print("You chose Poha.")
        elif c.capitalize() == "Aloo Poori":
            print("You chose Aloo Poori.")
        elif c.capitalize() == "Chole Bhature":
            print("You chose Chole Bhature.")
        else:
            print("Invalid input. Please choose a valid dish.")
    else:
        print("Invalid input. Please choose a valid cuisine.")
    print("Thank you for choosing Breakfast!")
elif a.capitalize() == "Lunch":
    print("You chose Lunch. Please choose a cuisine:")
    b = input("Enter 'Indian', 'Chinese', 'Italian', or 'Mexican': ")
    if b.capitalize() == "Indian":
        print("You chose Indian. Please choose a dish:")
        c = input("Enter 'Biryani', 'Rajma Chawal', 'Paneer Butter Masala with Naan', or 'Dal Makhani with Rice': ")
        if c.capitalize() == "Biryani":
            print("You chose Biryani.")
        elif c.capitalize() == "Rajma Chawal":
            print("You chose Rajma Chawal.")
        elif c.capitalize() == "Paneer Butter Masala with Naan":
            print("You chose Paneer Butter Masala with Naan.")
        elif c.capitalize() == "Dal Makhani with Rice":
            print("You chose Dal Makhani with Rice.")
        else:
            print("Invalid input. Please choose a valid dish.")
    elif b.capitalize() == "Chinese":
        print("You chose Chinese. Please choose a dish:")
        c = input("Enter 'Veggie Fried Rice', 'Chow Mein', 'Wonton Soup', or 'Egg Foo Young': ")
        if c.capitalize() == "Veggie Fried Rice":
            print("You chose Veggie Fried Rice.")
        elif c.capitalize() == "Chow Mein":
            print("You chose Chow Mein.")
        elif c.capitalize() == "Wonton Soup":
            print("You chose Wonton Soup.")
        elif c.capitalize() == "Egg Foo Young":
            print("You chose Egg Foo Young.")
        else:
            print("Invalid input. Please choose a valid dish.")
    elif b.capitalize() == "Italian":
        print("You chose Italian. Please choose a dish:")
        c = input("Enter 'Spaghetti Bolognese', 'Veggie Pizza', 'Lasagna', or 'Fettuccine Alfredo': ")
        if c.capitalize() == "Spaghetti Bolognese":
            print("You chose Spaghetti Bolognese.")
        elif c.capitalize() == "Veggie Pizza":
            print("You chose Veggie Pizza.")
        elif c.capitalize() == "Lasagna":
            print("You chose Lasagna.")
        elif c.capitalize() == "Fettuccine Alfredo":
            print("You chose Fettuccine Alfredo.")
        else:
            print("Invalid input. Please choose a valid dish.")
    elif b.capitalize() == "Mexican":
        print("You chose Mexican. Please choose a dish:")
        c = input("Enter 'Veggie Tacos', 'Quesadillas', 'Burrito', or 'Nachos': ")
        if c.capitalize() == "Veggie Tacos":
            print("You chose Veggie Tacos.")
       