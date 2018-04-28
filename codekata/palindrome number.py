num = (input("Enter a number: ")) 
rev = reversed(num) 
if list(num) == list(rev): 
    print("Palindrome number") 
else: 
    print("Not Palindrome number")
