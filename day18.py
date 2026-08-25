# 1. login function jo ek dictionary leta hai
def login(user_dict):
    print("Testing:", user_dict["username"])

# 2. test_data list — isme 3 dictionaries hain
test_data = [
    {"username": "admin", "password": "1234", "expected": "Pass"},
    {"username": "invalid", "password": "1234", "expected": "Fail"},
    {"username": "guest", "password": "", "expected": "Fail"}
]

# 3. for loop — har dictionary ko login() function me bhejo
for data in test_data:
    login(data)