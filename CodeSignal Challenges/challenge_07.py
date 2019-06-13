# https://app.codesignal.com/challenge/HHKmRM9PLczxAFFTy
'''
An email address such as "John.Smith@example.com" is made up of a local part
("John.Smith"), an "@" symbol, then a domain part ("example.com").
The domain name part of an email address may only consist of letters, digits,
hyphens and dots. The local part, however, also allows a lot of different
special characters. Here you can look at several examples of correct and
incorrect email addresses.
Given a valid email address, find its domain part.

Example
For address = "prettyandsimple@example.com", the output should be
findEmailDomain(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
findEmailDomain(address) = "codesignal.com".
'''


def findEmailDomain(address):
    return address[address.rfind("@")+1:]


def findEmailDomain(address):
    return address.split("@")[-1]


address = ["prettyandsimple@example.com", "fully-qualified-domain@codesignal.com",
           "\" \"@space.com", "someaddress@yandex.ru",  "\" \"@xample.org", "\"much.more unusual\"@yahoo.com",
           "\"very.unusual.@.unusual.com\"@usual.com", "admin@mailserver2.ru", "example-indeed@strange-example.com",
           "very.common@gmail.com"]

for i, j in enumerate(address, 1):
    print(f"Test:{i} -> Ans: {findEmailDomain(j)}")
