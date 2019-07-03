str = "My name is Binod"
print(str)

#[startingIndex:endingIndex]=> string slicing using slice operator []
print(str[11:16])

#[:index]=> slicing a range of string using[:last_target_index]
print(str[:7]) # prints from 0 to 6 index

#[index:] => prints characters from the target index
print(str[3:]) #begings from 3 index to the end

#[:] prints from begining to end
print(str[:])

#[:-index] => prints the whole string excluding the defined last indexed characters
print(str[:-5])

# [-startIndex:-endIndex] => prints the last characters excluding character(s) backward from the end.
print('The characters from the middle: ', str[-5:-2])

# [index:index] => prints empty
print('The string is: ',str[1:1])

'''-----------------------String Concatenation------------------------'''
stat1 = "Do you know me, "
stat2 = "Binod?"
strConcat = stat1 + stat2
print('The concatenated string: ', strConcat)

# string * number => it repeats the string for desired number of times.
print("The string multiplied: ", stat2 * 3)

'''------------f-Strings-------------'''
# f,{} => the pair helps to print variables value using variable name inside the curly braces
age = 36
name = 'Binod'
have = 2500
print(f'{name} is {age} years old.')

'''-----%operator----%f(float),%s(string),%d(int)-----'''
print("%s is %d years old and he has %f " %(name, age, have))

'''--------escape sequence----linefeed----tab"'''
print("Tab indention: ",'Binod\tShrestha')
print("New Line: ",'Binod\nShrestha')

'''----------String Functions()----------'''
#strip() => removes space at the begining and end of a string
strWithSpace = '     Happy Canada Day 2019        '
print('An example that removes whitespace: ', strWithSpace.strip())

#An example with space at the begining
strWithSpaceBegining = '               I love coding.'
print('An example that removes whitespace at the begining: ', strWithSpaceBegining.strip())


#An example with space at the end
strWithSpaceEnd = 'I am enjoying learing Python.                 '
print('An example that removes whitespace at the end: ', strWithSpaceEnd.strip())

#lower() and upper() => chages character to lower or upper case respectively
'''----lowercase----'''
lowerStr ='PYTHON IS AMAZING'
print('An example that chages uppercase characters into lowercase: ', lowerStr.lower())

'''---uppercase----'''
upperStr = 'python is amazing'
print('An example that chages lower case characters into uppercase: ', upperStr.upper())

'''---------find()---------'''
word = 'communication'
print(word.find('tion')) #return 9 as the 'tion' begins from that index

'''-------Membership operator---------'''
mem = 'tha' in 'Shrestha'
print(mem)

myList = ['HTML', 'CSS', 'JQUERY', 'PHP']
print('"CSS" is the member of myList: ', 'CSS' in myList)
print('"ES6" is not the memeber of myList: ', 'ES6' not in  myList)

'''------Identity operator----'''
identity = 'binod' is 'BINOD'
print('"binod" and "BINOD" are similar: ', identity)

identity2 = 'binod' is 'binod'
print('"binod" and "binod" are similar: ', identity2)

identity3 = 'binod' is not 'BINOD'
print('"binod" and "BINOD" are not similar: ', identity3)

