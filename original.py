#!/usr/bin/env python

#This is the original code used to create the function ip_valid.py

import sys
  

not_done = True


while not_done:

    ip_addr = raw_input("\n\nEnter IP Address: ")

    valid_ip = True

    octets = ip_addr.split(".")

    if len(octets) != 4:
    	print "\nOooops, you do not have 4 octets - try again!"
    	continue


    for i,octet in enumerate(octets):

        try:
            octets[i] = int(octet)

        except ValueError:
	    valid_ip = False


    if not valid_ip:
        print "\nYou entered an octet that was not an interger (or blank)", \
              "octet) - that's not going to work!"
	continue


    first_octet, second_octet, third_octet, fourth_octet = octets



    for octet in (first_octet, second_octet,third_octet,fourth_octet):
        if (octet < 0) or (octet > 255):
            valid_ip = False


    if valid_ip:
        not_done = False
    else:
        print "\nYou must enter a number between 1 - 255, please try again!"


print "\n\nThe IP address is vaile: %s\n" % ip_addr	
