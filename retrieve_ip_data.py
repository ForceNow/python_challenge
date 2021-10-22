# Parser IP from text file included IPs
# Command line argument parser
# main() function

# Imports modules
import re
import geo
import rdap
import argparse
import json


# function to extract the text file to ip list. It takes file as a argument.
def ip_extractor(text_file):
    # open text_file function and alias as f.
    with open(text_file) as f:
        # read lines in text file and save to file_string
        file_string = f.readlines()
    # regular expression pattern to find ip addresses.
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    # define the empty list to use it in for loop.
    ip_list = []
    # for loop to iterate through saved text lines in file_string.
    for line in file_string:
        # check if pattern match the in the string to avoid None value.
        if pattern.search(line) is not None:
            # save all found matches to the ip pattern and save into list.
            ip = re.findall(pattern, line)
            # add ip list to the end of ip_list variable
            ip_list.extend(ip)

    # return the list of ips
    return ip_list


def main():

    # create Argument Parser
    parser = argparse.ArgumentParser(description="Welcome to IP Geo and RDAP search software\n")

    # define arguments provided in the cmd.
    # argument ip_from is the position of the ip in the list. The function will iterate from provided number.
    parser.add_argument('--ipfrom', default=1, type=int, help='This argument takes integer from 1 to 4999.')
    # argument ip_to i the position of the ip in the list. The function will iterate to provided number.
    parser.add_argument('--ipto', default=2, type=int, help='This argument takes int value from 2 to 5000')
    parser.add_argument('-f', '--upload-file', help='This argument takes text file with IP addresses')

    # create subparser object to split functionality.
    subparsers = parser.add_subparsers(
        title="run GEO and RDAP IP search",
        description="This module return IPs GEO information.",
        dest="method",
        help="To run GEO IP module run as function with geoip parameter."
    )

    geoip = subparsers.add_parser('geo')
    geoip.add_argument('--ipfrom', default=1, type=int, help='This argument takes integer from 1 to 4999.')
    geoip.add_argument('--ipto', default=2, type=int, help='This argument takes int value from 2 to 5000')
    geoip.add_argument('-f', '--upload-file', help='This argument takes text file with IP addresses')

    geoip = subparsers.add_parser('rdap')
    geoip.add_argument('--ipfrom', default=1, type=int, help='This argument takes integer from 1 to 5000.')
    geoip.add_argument('--ipto', default=2,
                       help='This argument takes True or False value. --rdap-search True '
                            'will return RDAP Ip information. Default: False')
    geoip.add_argument('-f', '--upload-file', help='This argument takes text file with IP addresses')
    # user provide arguments in command line. The parse_args() function will return the values of those arguments.
    args = parser.parse_args()
    # the user can specify the command (method) in command line.
    # The geo command will run function to pull the geo ip data.
    if args.method == "geo" and (int(args.ipfrom) >= 1 and int(args.ipto) <= 5000):
        for i in range(int(args.ipfrom) - 1, int(args.ipto) - 1):
            ip = ip_extractor(args.upload_file)[i]
            print("Address IP: " + ip)
            print(json.dumps(geo.ip_geo_retrieve(ip), indent=4, sort_keys=True))
    # The rdap method will run function to pull RDAP ip data.
    elif args.method == "rdap" and (int(args.ipfrom) >= 1 and int(args.ipto) <= 5000):
        for i in range(int(args.ipfrom) - 1, int(args.ipto) + 1):
            ip = ip_extractor(args.upload_file)[i]
            print("Address IP: " + ip)
            print(json.dumps(rdap.ip_rdap_retrieve(ip), indent=4, sort_keys=True))
    # If user not provide any command the program will run both functions.
    else:
        for i in range(int(args.ipfrom) - 1, int(args.ipto) - 1):
            ip = ip_extractor(args.upload_file)[i]
            print("Address IP: " + ip)
            print("\n Geo information\n")
            print(json.dumps(geo.ip_geo_retrieve(ip), indent=4, sort_keys=True))
            print("RDAP information\n")
            print(json.dumps(rdap.ip_rdap_retrieve(ip), indent=4, sort_keys=True))

# This define decide what is the main function and run first in command line trigger.
if __name__ == "__main__":
    main()
