# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:52:51 2017

@author: Yiyang Zhou
"""
import re
import string

test1= "my phone number is 612-516-2045, and my email address is blabla@gmail.com, my address is 3200 College Park Ave. "
test2 = '''Hi, Mr. Sam D. Richards lives here, 44 West 22nd Street, New York, NY 12345-4567. Can you contact him now? If you need any help, call me on 123-456-7891.'''
test3 = '''Hi, Mr. Sam D. Richards lives here, 44 West 22nd Street, New York, NY 12345-3456. Can you contact him now? If you need any help, call me on 123-456-7891'''
test4 = '''call me at 123 456 7891.'''
test5 = '''call me at  (+1) 123 456 7891'''
#idea: remove all punctuation, only read 10 digits consecutive number

"""
def check_phone_number(string_to_search):
    regular_expression = re.compile(r"\(?"  # open parenthesis
                                        r"(\d{3})?"  # area code
                                        r"\)?"  # close parenthesis
                                        r"[\s\.-]{0,2}?"  # area code, phone separator
                                        r"(\d{3})"  # 3 digit exchange
                                        r"[\s\.-]{0,2}"  # separator between 3 digit exchange, 4 digit local
                                        r"(\d{4})",  # 4 digit local
                                        re.IGNORECASE)
    result = re.search(regular_expression, string_to_search)
    if result:
        result = result.groups()
        result = "-".join(result)
    print (result)

def check_phone_number(string_to_search):
    regular_expression = re.compile(r"\(?"  # open parenthesis
                                        r"(\d{3})?"  # area code
                                        r"\)?"  # close parenthesis
                                        r"[\s\.-]{0,2}?"  # area code, phone separator
                                        r"(\d{3})"  # 3 digit exchange
                                        r"[\s\.-]{0,2}"  # separator between 3 digit exchange, 4 digit local
                                        r"(\d{4})",  # 4 digit local
                                        re.IGNORECASE)
    result = re.search(regular_expression, string_to_search)
    if result:
        result = result.groups()
        result = "-".join(str(v) for v in result)
    print (result)


def check_phone_number(string_to_search):
    regular_expression = re.compile(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", re.IGNORECASE)
    result = re.search(regular_expression, string_to_search)
    if result:
        result = result.group()
    print (result)
"""

def check_phone_number10(string_to_search):
    string_to_search2 = "".join(c for c in string_to_search if c not in ('!','.','-','(',')',' ','+',))
    result = re.findall(r"\d{10}", string_to_search2)                   
    result = ''.join(result)
    return (result)

def check_phone_number11(string_to_search):
    string_to_search2 = "".join(c for c in string_to_search if c not in ('!','.','-','(',')',' ','+',))
    result = re.findall(r"\d{11}", string_to_search2)                   
    result = ''.join(result)
    result = "+" + result[0] + " " + result[1:11]
    return (result)

def check_phone_number(string_to_search):
    try:
        return check_phone_number11(string_to_search) 
    except:
        return check_phone_number10(string_to_search)


#Testing function step by step
temp1 = "".join(c for c in test1 if c not in ('!','.','-','(',')','+',' '))
temp2 = re.findall(r"\d{10}", temp1)
temp2 = ''.join(temp2)
if len(temp2) == 10:
    print (temp2)
result = re.findall(r"\d{11}", temp1)
strg = ''.join(result)
result1 = "+" + strg[0] + " " + strg[1:11]
print (result1)

check_phone_number(test1)
check_phone_number(test2)
check_phone_number(test3)
check_phone_number(test4)
check_phone_number(test5)


def check_email(string_to_search):
    regular_expression = re.compile(r"[A-Z0-9!#'$%&*+-/=?^._`{|}~]+@[A-Z0-9]+[-]?[A-Z0-9]+\.[A-Z]{2,4}", re.IGNORECASE)
    result = re.search(regular_expression, string_to_search)
    if result:
        result = result.group()
    print (result)

check_email(test)
check_email(test2)
check_email(test3)

