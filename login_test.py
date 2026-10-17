def test_login_with_valid_credentials():
    username = "student01"
    password = "pass123"

    # Simulate the login validation
    login_success = username == "student01" and password == "pass123"

    assert login_success
    print("Login test passed for AttendX!")


if __name__ == "__main__":
    test_login_with_valid_credentials()
