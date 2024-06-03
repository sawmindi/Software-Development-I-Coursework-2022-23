#Date- 01st Dec 2022

def credits_check(level):
    while True :
        try :
            credit = int(input("Please enter your credit at " + level + ": "))
            if credit >=0 and credit <= 120 and credit%20 == 0 :
                return credit
            else:
                print("Out of range.\n")
        except ValueError:
            print("Interger required\n")
            continue

progress = 0
trailer = 0
retriever = 0
exclude = 0
#part2_list = []
file = open("part2_data.txt", "w")# Open the file for writing

while True :
    Outcome = None
    passed_credits  = None
    deferred_credits = None
    failed_credits  = None
    while True:
        passed_credits  = credits_check("pass")
        deferred_credits = credits_check("defer")
        failed_credits   = credits_check("fail")

         # Calculate the total credits to ensure it equals 120
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
    print(Outcome)
    #print on the file
    file.write(Outcome + " - " + str(passed_credits ) + ", " + str(deferred_credits) + ", " + str(failed_credits ) + "\n")
    print("\nWould you like to enter another set of data?")
    staff = input("Enter 'y' for yes or 'q' to quit and view results: ")
    
    if staff == "q":
        break
    else :
        continue

# Close the file after writing all data
file.close()

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
print("Part 3:")
file = open("part2_data.txt")
print(file.read())
