# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Date: 20/04/2023

prgress_trailer=0
progress=0
exclude=0
Module_retriever=0
count=1
credit_values=[0, 20, 40, 60, 80, 100, 120] #credit values list
progress_data=[] #crete empty list

while True:                                                                                   
    while (count==1):
        try:
            
            while True:
                pass_credits=int(input("Please enter your credits at pass:- "))  #getting pass credit
                if pass_credits in credit_values: 
                    break
                else:
                    print("Out of range.")
            while True:
                defer_credits=int(input("Please enter your credits at defer:- ")) #getting defer credit
                if defer_credits in credit_values:
                    break
                else:
                    print("Out of range.")
            while True:
                fail_credits=int(input("Please enter your credits at fail:- ")) #getting fail credit
                if fail_credits in credit_values:
                    break
                else:
                    print("Out of range.")
                    
        except (ValueError):
            print("Integer required")
            continue

        def total_credits(pass_credits,defer_credits,fail_credits): #create function
            return pass_credits+defer_credits+fail_credits

        z=total_credits(pass_credits,defer_credits,fail_credits)  #call total credits function 
        if z != 120:  #check if total credits equal 120
            print("Total incorrect.")
            continue
        
        else:  #search result
            X=(pass_credits+defer_credits)-fail_credits                                                
            if pass_credits==120:
                print("progress")
                progress=progress+1
                progression="progress"

            elif pass_credits==100:
                print("Progress (module trailer)")
                prgress_trailer=prgress_trailer+1
                progression="Progress (module trailer)" 
                

            elif X<0:
                print("exclude")
                exclude=exclude+1
                progression="exclude"

            else:
                print("Module retriever")
                Module_retriever=Module_retriever+1
                progression="Module retriever"
            count=count+1

            progress_data.append([progression, pass_credits, defer_credits, fail_credits]) #adding data to the progress data list
            
            
    count=count-1
    print(" ")
 
    print ("Would you like to enter another set of data?")                                              
    user_input = input("Enter 'y' for yes or 'q' to quit and view results: ") #asking the user to decide whether to proceed
    if user_input == 'q':
        break
    elif user_input == 'y':
        continue
                                                                                                          
print("-"*60,"\n")   
print("Histogram")


print("Progress  ",progress," :",progress*"*")
print("Trailer",prgress_trailer," :",prgress_trailer*"*")
print("Retriever ",Module_retriever," :",Module_retriever*"*")
print("Excluded  ",exclude," :",exclude*"*")

Y=progress+prgress_trailer+Module_retriever+exclude                                                       
print(Y,"outcomes in total")

print("-"*60,"\n") 

print("Part 2:"'\n')
f= open('text.txt', 'w') #opening the text.txt file for writing

print("\nStored Data:")
for data in progress_data:
    print(data[0]," - ", data[1],",", data[2],",", data[3]) #showing the obtained data and informationin the form of a list
    f.write(str(data[0])+" - "+str (data[1])+","+ str(data[2])+","+str(data[3])+"\n") #writing to the text file
f.close() #close the text.txt file

print("\n")
print("Part 3:",'\n')
f = open ('text.txt','r') #read the text.txt file
print(f.read()) #print the text
f.close() 
