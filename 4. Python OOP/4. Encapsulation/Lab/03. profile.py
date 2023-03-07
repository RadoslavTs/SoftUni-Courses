class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        length = len(value)
        message = "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
        length = len(value)
        if length >= 8 and not value.lower() == value and any(x.isdigit() for x in value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


profile_with_invalid_password = Profile("Username", "Passw0rd")
print(profile_with_invalid_password)