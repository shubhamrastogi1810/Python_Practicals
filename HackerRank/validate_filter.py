"""You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores [a-z],[A-Z],[0-9],[_-].
The website name can only have letters and digits [a-z],[A-Z],[0-9].
The extension can only contain letters [a-z],[A-Z].
The maximum length of the extension is 3. 

fun has the following paramters:

    string s: the string to test

Returns

    boolean: whether the string is a valid email or not

Input Format

The first line of input is the integer N, the number of email addresses.
N lines follow, each containing a string.

Constraints

Each line is a non-empty string.

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""

def fun(s):
    values = [45,95]
    for i in range(48,58):
        values.append(i)
    for i in range(65,91):
        values.append(i)
    for i in range(97,123):
        values.append(i)
    
    s = s.split('@')
    extent = s[-1].split('.')
    
    if len(s) != 2 or '' in s:
        return False
    valid_name = list(map(lambda x: True if ord(x) in values else False,s[0]))
    extent = s[-1].split('.')
    values.remove(45)
    values.remove(95)
    valid_website = list(map(lambda x: True if ord(x) in values else False,extent[0]))
    valid_extention = False
    if len(extent[-1]) <= 3:
        valid_extention = True
    if valid_extention:
        if False in valid_name or False in valid_website:
            return False
        else:
            return True
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
