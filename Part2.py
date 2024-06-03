#Date- 30th Nov 2022


def credits_check(level):
    while True:
        try:
            credit=int(input("Please enter your credits at " + level + ": "))
            if credit >=0 and credit <= 120 and credit%20==0 :
                return credit
            else:
                print("Out of range.\n")
        except ValueError:
            print("Interger required\n")
            continue
progress=0
trailer=0
retriever=0
exclude=0
part2_list=[]# List to store outcomes and credits

while True:
    outcome = None
    passed_credits = None
    deferred_credits = None
    failed_credits = None
    while True:
        passed_credits=credits_check("pass")
        deferred_credits=credits_check("defer")
        failed_credits=credits_check("faild")
        total=passed_credits + deferred_credits + failed_credits
        if total !=120:
            print("Total is incorrect.\n")
            continue
        else:
            if passed_credits==120:
                outcome="Progress"
                progress +=1
            elif passed_credits>=100:
                outcome="Progress (module trailer)"
                trailer +=1
            elif (passed_credits + deferred_credits)>=60:
                outcome="Module retriever"
                retriever +=1
            else:
                outcome="Exclude"
                exclude +=1
            break
        
    print(outcome)
    #part2_list.append([outcome,passed_credits,deferred_credits,failed_credits])
    part2_list.append(outcome + " - " + str(passed_credits ) + ", " + str(deferred_credits) + ", " + str(failed_credits))
    print("\nWould you like to enter another set of data?")
    staff = input("Enter 'y' for yes or 'q' to quit and view results: ")
    
    if staff == "q":
        break
    else :
        continue

print("------------------------------------------------------------")
print("Histogram")
print("Progress", progress, "\t: ", "*" * progress)
print("Trailer", trailer, "\t: ", "*" * trailer)
print("Retriever", retriever, "\t: ", "*" * retriever)
print("Exclude", exclude, "\t: ", "*" * exclude)
total = progress + trailer + retriever + exclude
print(total, "outcomes in total")
print("------------------------------------------------------------")

'''
for staff in range (len(part2_list)):
  print(part2_list[staff][0] + "-" , end=" ")
  for x in range (1,len(part2_list[staff])-1):
        print(str(part2_list[staff][x]) + "," , end=" ")
  print(part2_list[staff][len(part2_list[staff])-1])
'''

print("Part 2:")
for staff in part2_list:
    print(staff)
    