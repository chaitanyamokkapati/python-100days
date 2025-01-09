# Python Lists

# Lists of Indian States
statesInIndia = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", 
          "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", 
          "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", 
          "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
          "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
          "Uttar Pradesh", "Uttarakhand", "West Bengal"]

print("----" * 5)

print(type(statesInIndia))

print("----" * 5)

# Pulling out data from List
print(f"First item in List was : {statesInIndia[0]}.")
print(f"Second item in List was : {statesInIndia[1]}.")
print(f"Last item in List was : {statesInIndia[-1]}.")
statesInIndia[-1] = "W B"
print(f"Last item in List was : {statesInIndia[-1]}. ***")

# .append function adds item at end of list.
# .extend function adds multiple lists items at end of list.