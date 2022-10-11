# ******************************
# Make your Code
# ******************************
inputvalues=input('Enter all elements values in acending order:')
numbers1=inputvalues.split()
inputvalue=int(input("Value"))
i=0
while i <len(numbers1):
    numbers1[i]=int(numbers1[i])
    if int(inputvalue)>=int(numbers1[i-1]) and int(inputvalue)<int(numbers1[i]):
        numbers1.insert(i,inputvalue)
    i=i+1
print(numbers1)
        
