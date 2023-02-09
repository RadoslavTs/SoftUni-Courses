from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidAtCountError(Exception):
    pass


email = input()

min_length = 4
name_pattern = r'[\w+\.]+'
domain_pattern = r'\.[a-z]+'
accepted_domains = [".com", ".bg", ".org", ".net"]

while email != "End":

    try:
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        if email.count("@") > 1:
            raise InvalidAtCountError("Email must have only one @ symbol!")

        if len(email.split("@")[0]) <= min_length:
            raise NameTooShortError("Name must be more than 4 characters")

        domain_part = email.split("@")[1]
        domain_search = findall(domain_pattern, email)
        if domain_search[-1] not in accepted_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        print("Email is valid")

    except IndexError:
        print("Email is invalid")

    email = input()

