#مشروع اله حاسبة ب إستخدام if , elif 
num1 = float(input("enter num1 :"))
oper = input("choose an operation (+ , - , *, / ) :")
num2 = float(input("enter num2 :"))
if oper == "+" : 
     result = num1 + num2
     print(num1 , "+" , num2 , "=" , result)
elif  oper == "-" : 
     result = num1 - num2
     print(num1 , "-" , num2 ,  "=" , result)
elif  oper == "*"  :
     result = num1 * num2
     print(num1 , "*" , num2 , "=" , result)
elif  oper == "/" : 
  if num2 != 0:
      result = num1 / num2
      print(num1 , "/" , num2 , "=" , result)
  else:
      print("Error! Division by zero")
else :
 print("invalid value")
