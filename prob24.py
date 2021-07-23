#Problem: Write a program to check whether a passed letter is a vowel or not.

letter=input('Enter a letter : ')
vow= ['a','e','i','o','u']
for i in vow:
    if letter== i:
        print('Letter is vowel')
        break

else:
    print('Letter is not vowel')
