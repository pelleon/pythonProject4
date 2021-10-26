# python3


import re


import re
def logs():
    mydata = []
    with open("logdata.txt", "r") as file:
        logdata = file.read()
    pattern="""
    (?P<host>.*)
    (\s+)
    (?:\S+)
    (\s+)
    (?P<user_name>\S+)
    (\s+)
    \[(?P<time>.*)\]\
    (\s)
    (?P<request>"(.)*")"""
    for item in re.finditer(pattern,logdata,re.VERBOSE):
        new_item = (item.groupdict())
        mydata.append(new_item)
    return(mydata)
print(len(logs()))