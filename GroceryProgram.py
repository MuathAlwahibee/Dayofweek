print("CSC 122-W1 - Program #1");
print("By <Student Muath Alwahibee> \n<due May 26>")

#We use the float statemnt to write a number with a decimal
item1 = float(input("\nEnter thr price of item #1: "))
item2 = float(input("Enter the price of item #2: "))
item3 = float(input("Enter the price of item #3: "))
item4 = float(input("Enter the price of item #4: "))
item5 = float(input("Enter the price of item #5: "))

a = (item1 + item2 + item3 + item4 + item5)
subtotal = a
sales_tax = a * 0.07
total = a * 0.07 + a

#We use format statemnt with ".2f" to have 2 digits only to the write of the decimal.
print ("\nSubtotal:",format(subtotal, '.2f'))
print ("Sales Tax:", format(sales_tax, '.2f'))

print ("Total:", format(total,'.2f'))
