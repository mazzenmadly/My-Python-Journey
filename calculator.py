# first_num = input()
 
# sec_num = input() 
# sign =  input() 



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


# first_num = 10
# sec_num =20
# sign ='+'
output = calculator(first_num, sec_num , sign)

print(output)
if output % 2 == 0:
        print("number  is even")
else:
        print("number is odd")

