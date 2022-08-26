import string
vanity_plate=input("Kindly enter your vanity plate: ")
s=""
is_valid=True
is_notvalid=False
if s in vanity_plate:
    while(len(vanity_plate))<= 6:
        print("valid vanity plate ")
    while (len(vanity_plate))>= 2:
        print("valid vanity plate")
    while vanity_plate[4][5]==int:
        print("valid vanity plate")
    while vanity_plate !=( ".", ","," "):
        print("valid vanity plate")
    while vanity_plate[0][1]==string:
        print("valid vanity plate")
else:
        print("invalid vanity plate")
print(vanity_plate)
