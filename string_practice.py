# Print the first letter of the following string

school = "McHenry County College"

print school[0]

# print the length of the school string
print len(school)

# Use a while loop to print each character (including spaces) in the school variable
index = 0
while index < len(school):
    letter = school[index]
    print letter
    index += 1

# Slice school into three variables, print the variables
first = (school[:7])
second = (school[8:14])
third = (school[15:])

print first
print second
print third

# use a while statement to search for the letter "e" in the
def find(school, ch):
    index = 0
    while index < len(school):
        if school[index] == ch:
            return index
        index += 1
    return -1
print "searched for and found letter e at location " + str(find(school, "e"))

# print the index of every location with the letter "e"

text = school
index = 0
while index < len(text):
        index = text.find('e', index)
        if index == -1:
            break
        print('e at location', index)
        index += 2 # +2 because len('e') == 2

# rembember, you should not use the same variable twice in the same program


# so if you used the variable index, use something else



# Write the code to count the number of times the letter y appears in the school variable
place = school
count = 0
for char in place:
    if char == 'y':
        count += 1

# print the total

print "their are " + str(count) + " y's in school variable"


# create a variable named college and store the upper case version of the variable school in it

a = "college"
a = a.upper()
print a

# check to see if Count is in the school variable
if "Count" in school:
    print "yes Count is in the school variable"
else:
    print "no Count is not in the school variable"
# check to see if count is in the school variable
if "count" in school:
    print "yes count is in school the school variable"
else:
    print "no count is not in the school variable"

