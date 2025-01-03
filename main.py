def base_converter():
   def is_valid_number_for_base(number, base):
        if base == 1:
            return all(char in '01' for char in number)
        elif base == 2:
            return all(char in '01234567' for char in number)
        elif base == 3:
            return number.isdigit()
        elif base == 4:
            return all(char in '0123456789abcdefABCDEF' for char in number)
        return False
      
    def binary_converter(binary_num):
        decimal_num = int(binary_num, 2)
        return {
            "octal": oct(decimal_num)[2:],
            "decimal": decimal_num,
            "hexadecimal": hex(decimal_num)[2:]
        }

    def octal_converter(octal_num):
        decimal_num = int(octal_num, 8)
        return {
            "binary": bin(decimal_num)[2:],
            "decimal": decimal_num,
            "hexadecimal": hex(decimal_num)[2:]
        }
       
    def decimal_converter(decimal_num):
        decimal_num = int(decimal_num)
        return {
            "binary": bin(decimal_num)[2:],
            "octal": oct(decimal_num)[2:],
            "hexadecimal": hex(decimal_num)[2:]
        }

    def hexadecimal_converter(hex_num):
        decimal_num = int(hex_num, 16)
        return {
            "binary": bin(decimal_num)[2:],
            "octal": oct(decimal_num)[2:],
            "decimal": decimal_num
        }
       
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
       
    if not is_valid_number_for_base(number, current_base):
        print("The number is not valid for the selected base!")
        return
       
    print("Select the base you want to convert to:")
    print("1. Binary")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")

    try:
        target_base = int(input("Enter your choice (1-4): "))
        if target_base not in {1, 2, 3, 4}:
            print("Invalid input! Please enter a number between 1 and 4.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number between 1 and 4.")
        return

    if current_base == target_base:
        print("The current base and the target base are the same. No conversion needed.")
        return

    conversions = {
        1: "binary",
        2: "octal",
        3: "decimal",
        4: "hexadecimal"
    }

   if current_base == 1:
        converted = binary_converter(number)
    elif current_base == 2:
        converted = octal_converter(number)
    elif current_base == 3:
        converted = decimal_converter(number)
    elif current_base == 4:
        converted = hexadecimal_converter(number)
    else:
        print("Invalid current base selection!")
        return

    target_base_name = conversions.get(target_base)

    if target_base_name and target_base_name in converted:
        result = converted[target_base_name]
    else:
        print("Invalid target base selection or conversion not possible!")
        return

    print(f"The number in {target_base_name} base is: {result}")

  
base_converter()
