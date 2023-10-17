f=input("Enter your first name: ")
l=input("Enter your last name: ")
def format_name(first_name,last_name):
    formatted_f_name=first_name.title()
    formatted_l_name=last_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
print(format_name(first_name=f,last_name=l))