#Date- 01st Dec 2022

def credits_check(level):
    while True :
        try :
            # Prompt the user to enter the credit at a specified level (pass, defer, or fail)
            credit = int(input("Please enter your credit at " + level + ": "))
            # Check if the entered credit is within the valid range (0, 20, 40, 60, 80, 100, 120)
            if credit >=0 and credit <= 120 and credit%20 == 0 :
                return credit
            else:
                print("Out of range.\n")
        except ValueError:
            print("Interger required\n")
            continue

# Initialize counters for each outcome
progress = 0
trailer = 0
retriever = 0
exclude = 0
# Dictionary to store the participant ID and their respective outcomes and credits
part_dict = {}

# Main loop to input data until the user chooses to quit
while True :
    Outcome = None
    passed_credits  = None
    deferred_credits = None
    failed_credits  = None
    ID = None
    while True:
        while True :
            ID= input("Please enter your ID number: ")
            if ID[0] =="w" and len(ID) ==8 :
                if ID in part_dict :
                    print("ID is already exists")
                    continue
                else:
                    break
            else:
                print("Invalid ID")
                    
                    
        passed_credits  = credits_check("pass")
        deferred_credits = credits_check("defer")
        failed_credits   = credits_check("fail")
        total = passed_credits  + deferred_credits + failed_credits 
        if total != 120 :
            print("Total is incorrect.\n")
            continue
        else :
            if passed_credits  == 120 :
                Outcome = "Progress"
                progress += 1
            elif passed_credits  >= 100 :
                Outcome = "Progress (module trailer)"
                trailer += 1
            elif (passed_credits  + deferred_credits) >= 60 :
                Outcome = "Module retriever"
                retriever += 1
            else :
                Outcome = "Exclude"
                exclude += 1
            break

    # Print the outcome for the current set of credits
    print(Outcome)
    # Update the dictionary with the participant ID and their outcome and credits
    part_dict.update({ID: Outcome + " - " + str(passed_credits) + ", " + str(deferred_credits) + ", " + str(failed_credits)})
    
    print("\nWould you like to enter another set of data?")
    staff = input("Enter 'y' for yes or 'q' to quit and view results: ")
    
    if staff == "q":
        break
    else :
        continue

# Print the histogram and total outcomes
print("------------------------------------------------------------")
print("Histogram")
print("Progress", progress, "\t: ", "*" * progress)
print("Trailer", trailer, "\t: ", "*" * trailer)
print("Retriever", retriever, "\t: ", "*" * retriever)
print("Exclude", exclude, "\t: ", "*" * exclude)
total = progress + trailer + retriever + exclude
print(total, "outcomes in total")
print("------------------------------------------------------------")

for staff in part_dict:
    print(staff + ":" + part_dict[staff], end =" ")
        
