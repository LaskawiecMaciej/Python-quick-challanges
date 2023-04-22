"""
Create a function that takes two number strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"
Notes
If any input is "" or None, return "Invalid Operation".
"""

#Odpowiedź:
def add(str1,str2):
    if (str1 == "" or str1 == None):
        print("invalid operation")
    elif (str2 == "" or str2 == None):
        print("invalid operation")
    else:
        str1=int(str1)
        str2=int(str2)
        sum = (str1+str2)
        sum = str(sum)
        return sum
#test:
print(add("", "20"))


