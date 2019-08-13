# OLKB List Spot

This is a simple python script to check how far out your order is from being shipped from the  
OLKB website. Execute once at the command line with your order number as a command line argument.  
After the initial run, the command line argument will not be required. This script just pulls the  
raw text list that is hosted on github, copies it to a file and then searches that file for your
order number. The command line will display when the list was last updated, as well what position your order is on the list. If your order number is not found in the list, the command line will display shipped. This script will generate 2 files, an
order_number.txt file and OLKBoutput.txt.

Enjoy your keyboard!
