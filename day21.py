def login(password):
    correct_password = "123"
    if password == correct_password:
        return "pass"
    else:
        return "fail"

passed_count = 0  # new counter
failed_count = 0  # new counter
total_count = 0   # new counter

try:
    file = open("users.txt", "r")
    for line in file:
        line = line.strip()
        if line == "":
            continue
        data = line.split(",")
        username = data[0].strip()
        password = data[1].strip()
        expected = data[2].strip()

        actual = login(password)
        total_count += 1  # count every test

        if actual == expected:
            print(f"{username}: PASS")
            passed_count += 1  # add to passed
        else:
            print(f"{username}: FAIL")
            failed_count += 1  # add to failed

    file.close()

    # This is the new report part
    print("\n============================")
    print("TEST REPORT")
    print("============================")
    print(f"Total Tests: {total_count}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print("============================")

except FileNotFoundError:
    print("Error: users.txt file not found")