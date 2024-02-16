# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Date: 20/04/2023

prgress_trailer=0
progress=0
exclude=0
Modle_retrive=0
count=1
T=[0, 20, 40, 60, 80, 100, 120] #credit values list
progress_data=[] #create list of progress data
dict={} #create dict

while True:                                                                                   
    while (count==1):
        try:
            uow_no=str(input("Enter student uow number :")) #getting uow no
            while True:
                pass_credits=int(input("Please enter your credits at pass:- ")) #getting pass credit
                if pass_credits in T:
                    break
                else:
                    print("Out of range.")
            while True:
                defer_credits=int(input("Please enter your credits at defer:- ")) #getting defer credit
                if defer_credits in T:
                    break
                else:
                    print("Out of range.")
            while True:
                fail_credits=int(input("Please enter your credits at fail:- "))#getting fail credit
                if fail_credits in T:
                    break
                else:
                    print("Out of range.")
                    
        except (ValueError):
            print("Integer required")
            continue
        
        def total_credits(pass_credits,defer_credits,fail_credits): #create function
            return pass_credits+defer_credits+fail_credits

        z=total_credits(pass_credits,defer_credits,fail_credits)  #call total credits function 
        if z != 120: #check if total credits equal 120
            print("Total incorrect.")
            continue
        
        else: #search result
            
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
                print("Modle retrive")
                Modle_retrive=Modle_retrive+1
                progression="Modle retrive"
            count=count+1

            progress_data.append([progression, pass_credits, defer_credits, fail_credits]) #adding data to the progress data list
            dict[uow_no]=progression, pass_credits, defer_credits, fail_credits #adding data to dict
            
            
    count=count-1
    print(" ")
 
    print ("Would you like to enter another set of data?")                                              
    user_input = input("Enter 'y' for yes or 'q' to quit and view results: ") #asking the user to decide whether to proceed
    if user_input == 'q':
        break
    elif user_input == 'y':
        continue
    
print("Part 4:")
for key,value in dict.items():
    print(f"{key}: {value[0]} - {value[1]}, {value[2]}, {value[3]} ",end=" ") #print dict
                                                                                                          
