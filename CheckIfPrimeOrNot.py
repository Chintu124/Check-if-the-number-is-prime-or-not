def CheckIfPrimeOrNot():
    num = int(input("Enter A Number: ")) #12


    if num>1:#Checks If The Number is Greater then 1


        for i in range(2,num):# Starts at two and checks until the number u entered


            if num % i==0: # 12 is divisible by 1 only so only 1 factor so not prime number

                print(num,  "is not a prime number") # This Gets Printed

            else: # Else If Num is Divisible by 1 and the number it self 
                print(num, "Is A prime number")    #THIS GETS PRINTED
    else: # If The Number is 1 then 

        print(num, "Is Not A Prime Number")# This Gets Printed

        if num<0: # if the number is less then zero

                print("please enter a positve number") #Print THis
                
CheckIfPrimeOrNot()# Calling the function