#!/usr/bin/env python

import sys


def valid_ip(ip_addr):

    src_octets = ip_addr.split(".")
    octets = []

    if len(src_octets) != 4:
        return (False, "oooops, you do not have 4 octets - try again!")

    for octet in src_octets:
        try:
            octets.append(int(octet))
        except ValueError:
            return (False, "A non-integral octet was found!")

    # there's a sneaky way to do the above...
    # octets = [int(x) for x in ip_addr.split(".")]
    # Less error handling of course, but list comprehensions
    # are nice from time to time for compact code...

    first_octet, second_octet, third_octet, fourth_octet = octets

    # you can kinda sorta do this atop octets too... instead of
    # repacking below

    for octet in octets:
        if (octet < 0) or (octet > 255):
            # can do this in one go...
            return (False,  "You must enter a number between 1 - 255!")

    # in terms of what to return... you might just want to return a tuple
    # of (bool, str|none) with two types:
    # (True, None), which says this is valid, or
    # (False, Str) where Str contains the reason why
    # I did the above here, but feel free to modify as needed!

    return (True, None)


not_done = True


if __name__ == "__main__":

    # slice argv from position >= 1
    for arg in sys.argv[1:]:
        (rc, msg) = valid_ip(arg)
        if rc:
            # I prefer format, but % works fine
            print "\n\nThe IP address is valid: {0}".format(arg)
        else:
            print "\n\nInvalid IP: {0}".format(msg)
