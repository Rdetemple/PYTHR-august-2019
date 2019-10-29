# You have a list of Disney characters and you want to find out if each of them contain i, o, or u in their names. Loop through each character
# in the list and print out the following:

disney_characters = ['simba', 'ariel', 'pumba', 'flounder', 'nala', 'ursula', 'scar', 'flotsam', 'timon']

# If the name contains a 'u', print out the name plus 'U are so Uniquely U!'
if 'u' in disney_characters:
    print ('U are so Uniquely U')

#I think I am missing the temporary way to save a variable in memory. 


# # Otherwise if the name contains an 'i', print out the name plus "I bet you're Impressively Intelligent!"
elif 'i' in disney_characters:
     print ("I bet you're Impressively Intelligent!")
#
# # Otherwise if the name contains an 'o', print out the name plus 'O My! How Original!'

elif 'o' in disney_characters:
     print ("O My! How Original!")
#
# # Otherwise, print the name plus "Ehh, a's and e's are so ordinary."
else:
     print ("Ehh, a's and e's are so ordinary.")
