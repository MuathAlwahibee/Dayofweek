print("CSC 122-W1 - Program #1");
print("By <Student Muath Alwahibee> \n<due June 15th>")

#Get the speed 
speed = int(input("\nWhat is the speed of the vehicale in mph? "))

#Get the number of hours
time = int(input("How many hours did you drive? "))

print("{:>0}{:>10}". format("Hour", "Distance"))

for hour in range(1, time+1):
    print("{:>0}{:>10}". format(hour, hour * speed))
