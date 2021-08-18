import re

with open('assets/potential-contacts.txt','r') as file:
    file = file.read()
    email_searh = re.findall("[\w.+-]+@[\w-]+\.[\w.-]+", file)
    # print(email_searh)
    with open('assets/Email-Searched.txt','w+') as file:
        for email in email_searh:
            file.write(f'{email_searh}')
    print(email_searh)