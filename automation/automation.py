import re

with open('assets/potential-contacts.txt','r') as file:
    file = file.read()
    email_searh = re.findall("[\w.+-]+@[\w-]+\.[\w.-]+", file)
    # print(email_searh)
    sorted_email = sorted(email_searh)
    with open('assets/email-Searched.txt','w+') as file:
        for email in sorted_email:
            file.write(f'{sorted_email}')
    print(sorted_email)

with open('assets/potential-contacts.txt','r') as file:
    file = file.read()
    phone_searh = re.findall("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", file)
    print(phone_searh)
    with open('assets/phone-Searched.txt','w+') as file:
        for phone in phone_searh:
            file.write(f'{phone_searh}')
    print(phone_searh)