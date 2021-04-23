print("Estimating the risk of death from coronavirus.")
list1 = []  
age = input("do you have elder 75 years old: ")
list1.append(age)
chronic = input("do you have a chronic disease(yes or no): ")
list1.append(age)
immune = input("are you have immune weak(yes or no): ")
list1.append(age)
smoke = input("do you smoke(yes or no): ")
list1.append(age)
if "yes" in list1:     # If there is already a "yes" in the list, the result is true of type bool.
                         # so the same as the "and" operator !!!!!!!
  print("You are in risky group")
elif "no" in list1:
  print("You are not in risky group")
else:

  print("please write just yes or no ")
