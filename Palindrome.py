def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	input_string=input_string.lower()
	input_string=input_string.replace(" ","")

	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if letter !="":
			new_string = input_string
			reverse_string = new_string[::-1]
	# Compare the strings
	if reverse_string==new_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
