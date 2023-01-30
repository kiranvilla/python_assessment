input_words_list = ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
print("Orginal list of strings:")
print(input_words_list) 
result = list(filter(lambda x: (x == "".join(reversed(x))), input_words_list)) 
print("\nList of palindromes:")
print(result) 