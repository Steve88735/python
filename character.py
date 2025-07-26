string=input("Please enter a word: ")
char = input("Please enter a letter: ")
i=0
count = 0
while(i<len(string)):
    if(string[i]==char):
        count = count + 1
    i= i+1
print("The total numberof occurances of Times",char, "has occured =",count)