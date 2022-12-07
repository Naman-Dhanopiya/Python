print("Hello! Welcome to Email Slicer")

data1 = input('Please enter your email I.D. :')
email = data1.strip()
# HERE, .strip() IS USED TO REMOVE WHITESPACE FROM BEGINNING AND END OF THE ORIGINAL (i.e. ENTERED) STRING !
# HERE, input of data1 string is first stored in a container/string (here, called email) !

username = email[:email.index('@')]
domain = email[email.index('@')+1:].upper()
# HERE, .index IS USED TO BRING THE INDEXING OUT AND ASSOCIATE IT WITH @ !
# HERE, .upper() IS USED TO CONVERT ALL LOWERCASE CHARACTERS IN A STRING (here, domain) TO UPPERCASE CHARACTERS !

print('Your username is:', username, 'and domain is:', domain)

print("Thank You!")
