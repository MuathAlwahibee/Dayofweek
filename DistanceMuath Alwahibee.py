print("CSC 122-W1 - Program #1");
print("By <Student Muath Alwahibee> \n<due June 15th>")

#Get the speed 
speed = int(input("\nWhat is the speed of the vehicale in mph? "))

#Get the number of hours
#We use int statment to write an integer number.
time = int(input("How many hours did you drive? "))

#We use {:>0}{:>10} after print statment to make space between the two words in format statment
print("{:>0}{:>10}". format("Hour", "Distance"))

#We use (for in) loop to repeat
for hour in range(1, time+1):
    print("{:>0}{:>10}". format(hour, hour * speed))
