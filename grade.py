# Program to read a students percentage mark and print out the corresponding grade.
# Taken from Andrew Beatty's week 4 lab on "if elif and else"

percentage = float(input("enter the percentage:"))
# print (percentage)

# be careful with 'ands' and 'ors'
if percentage < 0 or percentage > 100:

    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know that it is greater than zero
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")   
elif percentage < 60: # between 50 and 59
    print ("Merit 1")     
elif percentage < 70: # between 60 and 69
    print ("Merit 2")
else: # the only option left is between 70 and 100
    print ("Distinction")