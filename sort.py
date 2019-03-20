#! /usr/bin/python3

# The script asks to input desired number of strings
# and then finds out which of them were the longest.

elements_number = input("Please, enter the number of elements: ") # Entering the number of strings.
elements = []                                                     # Creating a list to store the strings.
largest_elements = []                                             # Creating a list to store the longest strings.

for i in range(0, int(elements_number)):                          # Starting a loop to input the strings.
	element = str(input("Please, enter the element " + str(i+1) + ": "))
	elements.append(element)

key = len(elements[0])                                            # Assuming the first string of the list as the longest

for i in range(0, len(elements)):                                 # Starting a loop to sort out the longest strings to the new list.
	if len(elements[i]) > key:                                # If i-string is longer than the previous one,
		key = len(elements[i])                            # it becomes assumed as the longest,
		largest_elements = []                             # the list is cleared
		largest_elements.append(elements[i])              # and i-string is added to the list of longest ones.
	elif len(elements[i]) == key:                             # If i-string's length is equal to the previous one
		largest_elements.append(elements[i])              # it's added to the list.
	else:                                                     # If i-string is shorter than previous one
		pass                                              # nothing happens.

print("The largest elements are: ")                               # Printing the list of the longest strings.
print(largest_elements)
