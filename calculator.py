def calculator(number_1, number_2, operator):
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2    
    elif operator == '/':
         result = number_1 / number_2
    return result
  
first_num = int(input())
sec_num = int(input() )
sign =  input() 
output = calculator(first_num, sec_num , sign)

print(output)
if output % 2 == 0:
        print("number  is even")
else:
        print("number is odd")

