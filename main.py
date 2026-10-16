total_homework= 4
original_count= total_homework
print (f"You have total {original_count} homeworks to complete today today!!\n")

completed_count= 0
task_no= 1 

while task_no<=total_homework:

    if task_no==1:
        next_task= "Math worksheet"

    elif task_no==2:
        next_task="Science reading"

    elif task_no==3:
        next_task="English writiing"

    else:
        next_task="Coding practice"

    answer=input (f"Have you completed {next_task}(yes/no):")

    if answer == "yes":
        completed_count+=1
        task_no+=1
        print ("\nAmazing! Homework task completed!")

    
    else:
        print ("No problem! Finish it quick and check again!")


    print ("\nHomework task remaining: ", total_homework- completed_count,"\n" )

print ("==========ALL HOMEWORK COMPLETE==========")
print ("Great work finishing your work today!!\n")


print ("=====Safe look at a INFINITE LOOP=====\n")

test_value=0
safety_counter=0

while test_value>=0:
    print ("This condition Never changes ; so it NEVER stops ")
    safety_counter+=1

    if safety_counter==3:
        print ("\nStoping here on purpose! - A  real INFINITE loop never stops on its own!")
        break

print ("\n======HOMEWORK COMPLETION SUMMARY======")
print ("\nHomework assigned today: ", original_count)
print ("Homework completed: ", completed_count)
print ("Homework Remaining: ",total_homework-completed_count)

print("======================================")
    
