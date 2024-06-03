#Date- 30th Nov 2022 


def credits_check(level):
    while True:
        try: 
            # Prompt the user to enter the credits at the specified level (pass, defer, or fail)
            credit = int(input("Please enter your credits at " + level + ": "))
            # Check if the entered credit is within the valid range (0, 20, 40, 60, 80, 100, 120)
            if credit >=0 and credit <= 120 and credit%20==0 :
                return credit
            else:
                print("Out of range.\n")
        except ValueError:
            print("Interger required\n")
            continue

# Initialize counters for each outcome
progress=0
trailer=0
retriever=0
exclude=0

while True:
    while True:
        passed_credits=credits_check("pass")
        deferred_credits=credits_check("defer")
        failed_credits=credits_check("fail")
        total=passed_credits + deferred_credits + failed_credits
        if total !=120:
            print("Total is incorrect.\n")
            continue
        else:
            if passed_credits==120:
                print("Progress")
                progress+=1
            elif passed_credits>=100:
                print("Progress (module trailer)")
                trailer+=1
            elif (passed_credits + deferred_credits)>=60:
                print("Module retriever")
                retriever +=1
            else:
                print("Exclude")
                exclude +=1
            break

    print("\nWould you like to enter another set of data?")
    staff=input("Enter 'y' for yes or 'q' to quit and view results: ")   
    if staff=="q":
        break
    else:
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
