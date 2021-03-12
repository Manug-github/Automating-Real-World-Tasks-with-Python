#!/usr/bin/env python3
import os
import sys
import shutil
import socket
import psutil
import emails


def check_disk_full():
    """Return True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage("/")
    percent_free = 100 * du.free / du.total
    if percent_free < 20:
        return True
    return False


def check_cpu_constrained():
    """"Return True if the cpu is having too much usage, False otherwise."""
    return psutil.cpu_percent(1) > 80


def check_ram():
    """"Return True if the available is lee than 500MB, False otherwise."""
    return psutil.virtual_memory().available/ 2**20 < 500


def checks_localhost():
    """Returns True if it fails to resolve local host, False otherwise"""
    try:
        socket.gethostbyname("127.0.0.1")
        return False
    except:
        return True


def main():
    checks = [
        (check_disk_full, "Error - Available disk space is less than 20%"),
        (check_cpu_constrained, "Error - CPU usage is over 80%"),
        (check_ram, "Error - Available memory is less than 500MB"),
        (checks_localhost, "Error - localhost cannot be resolved to 127.0.0.1"),
    ]

    for check, msg in checks:
        if check():
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            subject = msg
            body =  "Please check your system and resolve the issue as soon as possible."
            message = emails.generate(sender, receiver, subject, body)
            emails.send(message)


if __name__ == "__main__":
    main()

