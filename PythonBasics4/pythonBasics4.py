# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE

   if(len(contacts) == len(emails)):
       x=0
       for key in contacts:
           contacts[key] = emails[x]
           x+=1
   return contacts

# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE

    if(len(contacts) == len(contact_info)):
        x = 0
        for key in contacts:
            y = {"email":contact_info[x][0],"phone":contact_info[x][1]}
            contacts[key] = y
            x+=1

    return contacts

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE

    a = []
    b = []
    c = []

    for key in contacts:
        b.append(key)
        a.append(contacts[key]["phone"])
        c.append(contacts[key]["email"])

    x = [c, a, b]
    return x

