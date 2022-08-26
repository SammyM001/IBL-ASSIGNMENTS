user_variable=input("Kindly input the name of your preferred variable: ")
user_variable=user_variable.lower()
user_variable= user_variable.replace("","_")
print(user_variable + "_" + user_variable)