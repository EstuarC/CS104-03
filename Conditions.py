temp = 0
temp= (int)(input("Please enter the current temperature:"))
while(temp!=999):
    if temp > 90:
        print("Wear Shorts")
        temp= (int)(input("Please enter the current temperature:"))
    elif temp > 70:
        print("Short sleeves are fine")
        temp= (int)(input("Please enter the current temperature:"))
    elif temp > 50:
        print ("Wear a jacket")
        temp= (int)(input("Please enter the current temperature:"))
    elif temp > 32:
        print("Wear a heavy coat")
        temp= (int)(input("Please enter the current temperature:"))
    else:
        print("Stay Inside")
        temp= (int)(input("Please enter the current temperature:"))


    
    



           
           
