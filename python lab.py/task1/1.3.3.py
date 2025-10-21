SQFT_PER_ACRE = 43560

length = int(input("Enter the length of the field in feet: "))
width = int(input("Enter the width of the field in feet: "))

acres = length * width / SQFT_PER_ACRE
print("The area of the field is", acres, "acres")
