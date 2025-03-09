# def multiply_two_numbers(num1, num2):
#     return num1 * num2

# result = multiply_two_numbers(4, 5)
# print(result) 


# def waheed(num1, num2):
#     return num1 if num1 > num2 else num2 if num2 > num1 else "Both numbers are equal"

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The greater number is:", waheed(num1, num2))




# def ben():
#     print("ADDTION")
#     a=int(input())
#     b=int(input())
#     print(a+b)
# ben()


# def waheed(mark):
#     print("4 arrer",mark)

# waheed("waheed all clear")    



# def hathim():
#     a=int(input())
#     if(a%2==0):
#         print("even")
#     else:
#         print("not even")    
# hathim()        


# def hathim(b):
    
#     if(b%2==0):
#         print("even")
#     else:
#         print("not even") 
# a=int(input())    

# hathim(a)       


# def mohan(r1,r2):
#     for i in range(r1,r2):
#         print(i)
    
# mohan(1,29)    

# def men():
#     return "the sigema men"
# boy=men()
# print(boy)





adim_username="waheed008"
adim_password="waheed008@@@"

username=input()
password=input()

def login():
    if(adim_username==username and adim_password==password):
        return "correct"
    else:
        return "worng"
a=login()
print(a)    