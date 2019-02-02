
def number_checker(num, check):
  "Function checks if a number is a multiple of 4 and is odd or even. "
  
  if num % 4 == 0:
      print(num, "Is a multiple of 4")
  elif num % 2 == 0:
      print(num, "Is an even number")
  else:
      print(num,"You picked an odd number.")

  if num % check == 0:
      print(num, "divide evenly by", check)
  else:
      print(num, "does not divide evenly by", check)
      
def main():
  # Get numeric input from user.
  num = int(input("Give me a number to check: "))
  check = int(input("give me a number to divide by: "))
  
  # Call function to check number.
  number_checker()
  
if __name__ == '__main__': main()    
