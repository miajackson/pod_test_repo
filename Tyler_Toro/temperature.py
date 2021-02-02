# Temperature converter
print("Temperature Converter")

# STEP 1
# 100 degrees f to c
print("STEP 1")
print("100 degrees f to c")

celsius_100 = (100 - 32)*(5/9)

print(celsius_100)

# the answer is 37.7777778. so its a  float

#STEP 2
# now, convert 0F degree to C
print("STEP 2")
print("converting 0F to C")

celsius_0 = (0-32)*(5/9)

print(celsius_0)

# the answer is -17.77777777777778

#STEP 3
# now we want to convert 34.2F to celsius, 
#saving variable
print("STEP 3")
print("without saving data, 34.2F=____C")
print((34.2-100)*5/9)

# answer is -36.55555555555556

# STEP 4
#convert 5C to F
print("STEP 4")
print("5 degrees C to F=")
print((5*1.8)+32)

#STEP 5, whats hotter 30.2C or 85.1F
print("STEP 5")
print("whats hotter 30.2C or 85.1F???")
''' Convert both to same type of temperature'''

temp1C = 30.2
temp1F = ((30.2)*1.8 + 32)
print("30.2 Celsius convereted to F =___")
print(temp1F)
# answer is 86.36
print("30.2C is hotter than 85.1F, because 86.36 > 85.1")

#Done

## Sending to Github now
