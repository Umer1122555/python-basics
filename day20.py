def login(username, password):
    # This is our fake system. Real one would be Selenium later
    # Rule: password "123" = Pass, everything else = Fail
    if password == "123":
        return "Pass"
    else:
        return "Fail"

try:
    file = open("users.txt", "r")
    print("Running Tests...\n")
    for line in file:
        data = line.strip().split(",")
        username = data[0]
        password = data[1]
        expected = data[2]  # What the test data says should happen
        actual = login(username, password)  # What our system actually does

        # The important QA part: Compare expected vs actual
        if expected == actual:
            print(username, ": PASS")
        else:
            print(username, ": FAIL - Expected", expected, "but got", actual)

    file.close()
except FileNotFoundError:
    print("error: users.txt not found")