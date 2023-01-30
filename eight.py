ask_input = True
while ask_input:
  try:
    value = int(input("Enter a valid integer: "))
    ask_input = False
  except ValueError:
    ask_input = True