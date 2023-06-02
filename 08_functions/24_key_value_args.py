"""
Sometimes we could send key args to our function
To define this type of params we must define as **kargs
"""


def make_customer(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


albert = make_customer('alber', 'einstein', country='eu', field='psisics')
frida = make_customer('frida', 'khalo', country='mx', field='painting')

print(albert)
print(frida)
