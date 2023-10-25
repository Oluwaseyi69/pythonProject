import json
# with open("account.txt", mode='w') as my_file:
#     my_file.write("001 esther 15\t Canada\n")
#     my_file.write("002 moyin 13\t Quebec\n")
#     my_file.write("003 precious 15\t Warri\n")
#     my_file.write("004 ashley 23\t Uyo\n")
#     my_file.write("005 grace 20\t Surulere\n")


# with open("../account.txt", mode='r') as file_obj:
#     print(file_obj.readlines())
#     file_obj.seek(0)
#     print(file_obj.readline())

accounts_dict= {'accounts':[
    {'account':100,'name':'jones', 'balance': 24.98},
    {'account':200,'name':'doe', 'balance': 345.67}]
}

with open('accounts.json', 'w') as accounts:json.dump(accounts_dict,accounts)

with open('accounts.json', 'r') as accounts:accounts_json = json.load(accounts)

with open('accounts.json', 'r') as accounts:print(json.dumps(json.load(accounts),indent = 4))

