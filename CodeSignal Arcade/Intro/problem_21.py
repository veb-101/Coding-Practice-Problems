# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso
'''
An IP address is a numerical label assigned to each device (e.g., computer,
printer) participating in a computer network that uses the Internet Protocol for
communication. There are two versions of the Internet protocol, and thus two
versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.
'''

import ipaddress


def isIPv4Address(s):
    p = s.split('.')
    return len(p) == 4 and all([n.isdigit() and 0 <= int(n) < 256 for n in p])


def isIPv4Address(s):
    try:
        ipaddress.ip_address(s)
        return True
    except:
        return False


print(isIPv4Address("172.16.254.1"))
print(isIPv4Address("172.316.254.1"))
print(isIPv4Address(".254.255.0"))
print(isIPv4Address("1.1.1.1a"))
