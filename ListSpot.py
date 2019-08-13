#!/usr/bin/env python3

import os
import sys
import requests

def get_order_number():
    order_num = ''
    if len(sys.argv) > 1:
        order_number = sys.argv[1]
        
        with open('./order_number.txt', 'w') as file:
            file.write(sys.argv[1])
            file.flush()
            
        order_num = sys.argv[1]
        return order_num

    elif os.path.exists("./order_number.txt"):
        
        with open("./order_number.txt") as file:
            order_num = file.readline()

    return order_num 


def get_file():
    req = requests.get('https://raw.githubusercontent.com/'
    + 'olkb/orders/master/README.md')    
    if not os.path.exists('OLKBoutput.txt'):
        open('OLKBoutput.txt', 'w').close()    

    my_file = open('OLKBoutput.txt', 'r+')
    my_file.write(req.text)
    req.close()
    my_file.flush()
    my_file.seek(0)
    return my_file

def get_order_status():
    order_num = get_order_number()
    print(order_num)
    if order_num != '' and order_num.isdigit():
        my_file = get_file()
        found_num = False

        for line in my_file:
            if '*This' in line:
                print(line)
            if order_num in line:
                print(line)
                found_num = True
                break
        if not found_num:
            print('The order has shipped')
    else: 
        print('An order number was never specified or is not the proper format')
get_order_status()

