x=input()
x=x.replace(" ","...")
print(x)
#why if i didn't give the x=x.replace(" ","...") it will not work?
#because the replace function does not change the original string, it returns a new string with the replacements. So if you want to see the changes, you need to assign the result back to x.
