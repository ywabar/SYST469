

class User:
    UsersList = []

    def __init__(self, age, gender, firstName, lastName):
        if len(firstName) == 0:
            if age.upper() == "M":
                self._firstName = "John"
            elif age.upper() == "F":
                self._firstName = "Jane"
        else:
            self._firstName = firstName
        if len(lastName) == 0:
            self._lastName = "Doe"
        else:
            self._lastName = lastName

        [self._age, self._gender] = [age, gender]
        User.UsersList.append(self)
        self._username = ""
        self._password = ""

    @property
    def firstName(self):
        return self._firstName

    @property
    def lastName(self):
        return self._lastName

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @property
    def username(self):
        return self._username

    @username.setter
    def password(self, value):
        self.username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def loginForm(self, usernameInput, passwordInput):
        if usernameInput == self._username and passwordInput == self._password:
            return True
        else:
            return False


def main():
    firstName = input("Enter a valid first name: ")
    while " " in firstName or len(firstName) == 0:
        firstName = input("ERROR: Enter a valid first name: ")
    lastName = input("Enter a valid last name: ")
    while " " in lastName or len(lastName) == 0:
        lastName = input("ERROR: Enter a valid last name: ")
    age = int(input("Enter a valid age (10-65): "))
    while age > 65 or age < 10:
        age = int(input("ERROR: Enter a valid age (10-65): "))
    gender = input("Enter a valid gender (M/F): ")
    while gender.lower() != "m" and gender.lower() != "f":
        gender = input("ERROR: Enter a valid gender (M/F): ")
    gender = gender.capitalize()
    username = input("enter a valid username: ")
    password = input('enter a valid password: ')
    currentUser = User(age, gender, firstName, lastName)
    currentUser._username = username
    currentUser._password = password
    print("Welcome "+currentUser.returnName()+"!")

    print(User.UsersList[0]._username)


if __name__ == '__main__':
    main()
