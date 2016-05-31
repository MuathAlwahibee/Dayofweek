age = int(input("How old are you? "));
 
if age <= 1:
    print ("infant");
else:
    print("Not infant");
    
if age > 1 and age < 13:
    print("child");
else:
    print("Not child");
    
if age >= 13 and age < 20:
    print ("teenager");
    
elif age >= 20:
    print("adult"); 

