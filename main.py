def base_converter():
   print("Welcome to the Base Converter")
   number = input("Enter the number: ")
   print("Select the current base of the number:")
   print("1. Binary")
   print("2. Octal")
   print("3. Decimal")
   print("4. Hexadecimal")
   
   try:
       current_base = int(input("Enter your choice (1-4): "))
        if current_base not in {1, 2, 3, 4}:
           print("Invalid input! Please enter a number between 1 and 4.")
           return
    except ValueError:
        print("Invalid input! Please enter a valid number between 1 and 4.")
        return

  
base_converter()
