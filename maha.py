# basic concepts of python
# nodes_count = 5
# graph_name = "my first network"
# points = ["a" ,"b","c","d" ]
# print(' name ?', graph_name)
# print("no of vertex", len(points))   
# print("i love mom")
# print(13*4)  
# #var = 5     
# # print(var)
# x =  y = z = 10 
# print('x == ' , x)
# print('y == ', y)
# print('z == ', z)
# name = ('maha')
# print(name)
# #int دا متغير للارقام 
# age = 3
# print(age)
# #float مخزن للاعداد الكسرية 
# gpa = 3.4
# print (gpa)
# #string مسئول عن النصوص ولكن النصوص لابد أن تكون بين علامات تنصيص
# name = ("maha abdallah")
# print(name)

# name = "reem"
# print('welcome ' + name) #بسيب مسافه قبل ال' علشان افصل بين الكلمتين

# nickname = " \" rawan\""#\ هذه وظيفتها لو حبيت أظهر فاصله او علامة تنصيص قبل الكلمة 
# print("hello " + nickname)
# #\n معناه سطر جديد 
# # modulus % علامه % تستخدم لايجاد باقي القسمه و ليكن 10%10 = صفر
# # small num% big num = small num 10%20 =10
# #big num % small num = big num 10%3= 10-3 =7-3=4-3=1
#**************************************************************************************
#مشروع اله حاسبة ب إستخدام if , elif 
# num1 = float(input("enter num1 :"))
# oper = input("choose an operation (+ , - , *, / ) :")
# num2 = float(input("enter num2 :"))
# if oper == "+" : 
#     result = num1 + num2
#     print(num1 , "+" , num2 , "=" , result)
# elif  oper == "-" : 
#     result = num1 - num2
#     print(num1 , "-" , num2 ,  "=" , result)
# elif  oper == "*"  :
#     result = num1 * num2
#     print(num1 , "*" , num2 , "=" , result)
# elif  oper == "/" : 
#  if num2 != 0:
#      result = num1 / num2
#      print(num1 , "/" , num2 , "=" , result)
#  else:
#      print("Error! Division by zero")
# else :
#   print("invalid value")
#***********************************************************************
# مشروع الكافيه ب استخدام if , elif , nasted if
# drink = input('what would you like to  drink( coffee or tea) ')
# if drink == 'coffee':
#     suger = input('Do you want black or with suger ? ')
#     if suger == 'black':
#         print ( 'black coffee')
#     elif suger == 'with suger':
#         print ( 'nice' )
#     else :
#         print ('sorry')
# if drink == 'tea':
#      typeoftea= input('what type do you want red or green ? ')
#      if typeoftea == 'green':
#         print ( 'green tea')
#      elif typeoftea == 'red':
#         print ( 'nice' )
#      else :
#         print ('sorry')
#*************************************************************************************************
# lists____________________________________________________________
# student = ['maha','naglaa','sania','noha','reem','rawan']# this is a list and it can have string or int or float
# print(student)
# print('list is ', student[2])# the counter starts of index 0
# print('list is ', student[-1])#-1 means the last element
# print('list is ', student[-2])#-2 means the element before the last element
# fruits = ['mango','banana','apple']#هذا الامر حتي السطر 81 يستطيع التبديل بين محتويات القائمة 
# print('Before',fruits)
# fruits[0] ='kiwi'
# print('After', fruits)
# fruits.append("watermelon")#  هذه الاداه لإضافة عنصر في القائمة في نهاية القائمة 
# print("after",fruits)
# fruits.insert(1,"date")#  هذه الاداه لإضافة عنصر في القائمة مع تحديد موضع الاضافة 
# print("After",fruits)
# fruits.remove("date") #هذا الامر لحذف عنصر من القائمة
# print("After",fruits)
# del fruits[1] #هذا الامر لحذف عنصر من القائمةبتحديد المكان
# print("After",fruits)
# fruits.pop(1) #هذا الامر لحذف عنصر من القائمة بتحديد موقعه
# print("After",fruits)
#**********************************************************************
#loops التكرار two sentences for , while
# جملة for________________________________________________________________
# for num in range (5):
#  print ('maha')
# for i in range (1,11):#أنا محتاجة يكتب من 1 إلي 10 فلاوم أزيد رقم 
#  print (i)
# word = "maha"#هنا كود علشان يطبع حروف الكلمة 
# for letter in word:
#  print (letter)
# total = 0 # أقصد أعمل عملية جمع الاعداد من 1 حتي 10
# for i in range  (1, 11):
#  total = total + i
# print ("total" , "=" , total )
#********************************************************************************
#جملة while __________________________________________________________
#جملة while تعمل بنظام الشرط طالما الشرط متحقق بينقذ الاوردر طالما الشرط غير متحقق خلاص بيتوقف 
# i = 1
# while i <= 5:
#     print(" maha")
#     i += 1 #لو لم أكتب هذه الجمله ستبقي جملة صاهمث تكرر اسم مها عدد لا نهائي من المرات لان طول الوقت ستظل i اقل من 5
# # حساب ال مضروب ب استخدام جملتي  for , while 
# num = 20 # by for 
# fact = 16 
# for i in range (16, num+1):
#     fact *= i
#     print("factorial", "=", fact)
# num = 5 #by while
# fact = 1
# i = num 
# while  i > 0 :
#     fact *= i
#     i -= 1
#     print("factorial", "=", fact)
# i = 0
# while i <= 10:
#     print (i) 
#     i += 2
#*******************************************************************
# جملة for by lists
# names=["maha", "reem", "rawan"]
# for n in names:
#     print(n)
# num=[1,2,3,4,5,6]
# for R in num:
#     print(R*2)# إضرب كل عدد داخل القائمة في 2
# #______________________________________________________________________    
# grade =[46, 57, 99,75,22]# جملة for لحساب عدد الناجحين 
# passed = 0
# for g in grade:
#     if g >= 50:
#         passed += 1
# print("no of passed student", "=", passed)
# #_________________________________________________________________
# grade =[46, 57, 99,75,22]# جملة for لحساب قيم الدرجات بعد إضاف بونص 5 درجات 
# new_gra = []#إعمل قائمة فاضيه 
# for g in grade:
#     bouns = g+5# هتزيد علي كل رقم جوا ال جي 5
#     new_gra.append(bouns)# ضع النواتج بتاعت البونص جوا القائمة الجديدة 
# print("original grades", "=", grade)
# print("grades after bounas", "=", new_gra)
#*************************************************************************
#break بتكسر جملة for or while 
# name=["maha","reem","rawan","naglaa"]
# for n in name:
#     if n == "rawan":
#         print("break the loop")
#         break
#     print(n)
# name=["maha","reem","rawan","naglaa"]#جملة continue تعني لو المتغير يساوي القيمة كمل جملة فور بدون هذه القيمة 
# for n in name:
#     if n == "rawan":
#         continue
#     print(n)  
# # هنكتب جملة بريك و كونتينيو داخل while
# i = 0
# while i<10 :
#     i += 1
#     if i == 3:
#         continue
#     if i == 7:
#         break
#     print (i)    
#*******************************************************************************************
# functions________________________________________________________________________________
# def greet ():# داله جوا الصندوق بكتب فيها الجمل وبعد كده بستدعيها بنفسي الدالة لابد أن تبدأ ب def
#     print('welcom')
#     print('hello')
# greet()# كده أنا بستدعي الدالة
# greet()# كده هينفذ محتويات الدالة مرتين 
# # function : parameter____________________________________________________________________
# def say (name):
#     print("welcome", name)
#     print("hi", name)
# say("ahmed")
# say("mohammed")
# #################################
# def say (name, age):
#     print("welcome", name)
#     print("your age", age)
# say("ahmed",24)
# say("mohammed",35)
# #################################
# def get_discount(price):
#     return price*0.5
# final_price = get_discount(1000)
# print("final price", "=" , final_price)
#**********************************************************************