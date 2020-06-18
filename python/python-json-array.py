import json

content=[{
    "username": "admin",
    "first_name": "",
    "last_name": "",
    "roles": "system_admin system_user",
    "locale": "en",
    "delete_at": 0,
    "update_at": 1511335509393,
    "create_at": 1511335500662,
    "auth_service": "",
    "email": "adminuser@cognizant.com",
    "auth_data": "",
    "position": "",
    "nickname": "",
    "id": "pbjds5wmsp8cxr993nmc6ozodh"
}, {
    "username": "chatops",
    "first_name": "",
    "last_name": "",
    "roles": "system_user",
    "locale": "en",
    "delete_at": 0,
    "update_at": 1511335743479,
    "create_at": 1511335743393,
    "auth_service": "",
    "email": "chatops@cognizant.com",
    "auth_data": "",
    "position": "",
    "nickname": "",
    "id": "akxdddp5p7fjirxq7whhntq1nr"
}]


for item in content:
    print("Name: {}\nEmail: {}\nID: {}\n".format(item['username'],item['email'],item['id']))
