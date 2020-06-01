import os
import sys, getopt

def main(argv):
    target_vlan = ''
    target_range = ''
    help_message = 'segmentation.py -v <target_vlan> -t <target_ip_range>'

    # Get options and arguments
    try:
        opts, args = getopt.getopt(argv,"hv:t:",["vfile=","tfile="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)

    # Check and parse arguments given
    for opt, arg in opts:
        if opt == '-h':
            print(help_message)
            sys.exit()
        elif opt in ("-v", "--vfile"):
            target_vlan = arg
        elif opt in ("-t", "--tfile"):
            target_range = arg
        elif opt == '':
            print(help_message)

    # Only run if arguments were given
    if opts != []:
        # Make a directory for nmap's output
        try:
            os.mkdir(target_vlan)
        except OSError:
            print("Creation of the directory %s failed " % target_vlan)
        else:
            print("Successfully created the directory %s " % target_vlan)

            # Run nmap commands in succession
            os.system("nmap -Pn -vvv -r -sS --reason --top-ports 1000 --max-retries 1 -oA " + target_vlan + "/nmap-sS-full." + target_vlan + " " + target_range)
            os.system("nmap -Pn -vvv -r -sU --top-ports 100 --reason --max-retries 0 -oA " + target_vlan + "/nmap-sU." + target_vlan + " " + target_range)
            os.system("nmap -vvv -sO -p 0-2,4,6,17,41-44,47,50,51,58-60,89 -oA " + target_vlan + "/nmap-sO-" + target_vlan + " " + target_range)

    else:
        print(help_message)


if __name__ == "__main__":
    main(sys.argv[1:])
