import ip_valid
# can also do: from ip_valid import valid_ip


ips = ["192.168.0.10", "167.206.112.3", "54.54.54.3", "foo.bar.baz.ba"]

for ip in ips:
    (rc, msg) = ip_valid.valid_ip(ip)
    if rc:
        # I prefer format, but % works fine
        print "\n\nThe IP address is valid: {0}".format(ip)
    else:
        print "\n\nInvalid IP: {0}".format(msg)

