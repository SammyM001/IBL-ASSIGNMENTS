Amount_payable=input("Kindly insert a coin: ")
if Amount_payable == int (25):
    result=int(50)-int(Amount_payable)
    result=print("You have 25 cents remaining")
elif Amount_payable == int(10):
     result=int(50)-int(Amount_payable)
     result=print("You have 40 cents to be paid")
elif Amount_payable == int(5):
     result=int(50)-int(Amount_payable)
     result=print("Kindly enter 45 cents more to buy coke")
elif Amount_payable ==int(50):
     result=int(Amount_payable)- int(50)
     result=print("We owe you" + result + "cents")
else:
     print("invalid amount")
