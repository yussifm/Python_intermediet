import re

isPhoneNumber = re.compile(r'\d{3} \d{3} \d{3} \d')

num = isPhoneNumber.search("my phone number is 054 246 009 8 ")

optmatch = re.compile(r'bat(wo)*man')
r1 = optmatch.search("I am a batman")
r2 = optmatch.search("I am a batwoman")
# print(r2.group())

xmasRegex = re.compile(r'\d+\s\w+')
xr = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(xr)
