# SYSUTIL by Alexander Abraham, 
# a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import psutil
import argparse
import datetime

def get_mem_usage():
    """
    This function returns the percentage
    of memory currently in use.
    """
    percentage = psutil.cpu_percent(interval=1)
    return percentage

def get_disk_usage():
    """
    This function returns the percentage
    of ROM memory currently in use.
    """
    total = psutil.disk_usage('/').total
    used = psutil.disk_usage('/').used
    perc = round(((used/total) * 100),1)
    return perc

def get_date():
    """
    This function returns the
    current date.
    """
    today = datetime.date.today()
    formatted = today.strftime("%d.%m.%Y")
    return formatted

def get_time():
    """
    This function returns the
    current time.
    """
    now = datetime.datetime.now()
    formatted = now.strftime("%H:%M:%S")
    return formatted

class Info:
    """
    The "Info" class encapsulates all of
    the statistics that Sysutil can display.
    """
    def __init__(self, mem, disk, date, time):
        """
        The standard method
        to create a new instance of a class.
        """
        self.mem = mem
        self.disk = disk
        self.date = date
        self.time = time

def get_info():
    """
    This function calls
    other functions for relevant
    statistics and puts them inside
    the "Info" class for easier retrival.
    """
    ram = get_mem_usage()
    disk = get_disk_usage()
    date = get_date()
    time = get_time()
    info = Info(ram, disk, date, time)
    return info

def cli():
    """
    Sysutil's CLI!
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', action='store_true')
    parser.add_argument('--time', action='store_true')
    parser.add_argument('--ram', action='store_true')
    parser.add_argument('--disk', action='store_true')
    info = get_info()
    args = parser.parse_args()
    if args.ram:
        print(info.mem)
    elif args.date:
        print(info.date)
    elif args.time:
        print(info.time)
    elif args.disk:
        print(info.disk)
    else:
        print('Inavlid argument supplied!')


def main():
    """
    We need a main
    method for readbility
    and because I come
    from C and Rust.
    """
    cli()

if __name__ == '__main__':
    """
    Execute the "main" function
    if Sysutil is called as a script.
    """
    main()

