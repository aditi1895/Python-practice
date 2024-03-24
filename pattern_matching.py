import numbers
import re
phoneregex = re.compile(r'(\d{3})-(\d{4})-(\d{3})')
group_match = phoneregex.search('My home number is 934-4567-983')
print(group_match.group(0))

# char_reg = re.compile(r'[a,z]|[A,Z]|[0,9]')
# group_match = char_reg.match("ABCDEFabcdef123450")
# print(group_match.group(). bool(group_match))

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    charRe = re.compile(r'(a)[0*|b*]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))

iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

def f(*args,**kwargs): print(args, kwargs)
f(1,2,3,"groovy",a=1,b=2,c=3, "groovy2")   