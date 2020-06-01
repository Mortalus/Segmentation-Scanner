import os
import sys, getopt

def main(argv):
    target_vlan = ''
    target_range = ''
    try:
        opts, args = getopt.getopt(argv,"hv:t:",["vfile=","tfile="])
        #print(opts, args)
    except getopt.GetoptError:
        print('segmentation.py -v <target_vlan> -t <target_ip_range>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('segmentation.py -v <target_vlan> -t <target_ip_range>')
            sys.exit()
        elif opt in ("-v", "--vfile"):
            target_vlan = arg
        elif opt in ("-t", "--tfile"):
            target_range = arg

    os.system("nmap -Pn -vvv -r -sS --reason --top-ports 1000 --max-retries 1 -oA nmap-sS-full." + target_vlan + " " + target_range)
    #os.system("nmap -Pn -vvv -r -sU --top-ports 100 --reason --max-retries 0 -oA nmap-sU." + target_range + " " + target_range)

if __name__ == "__main__":
    main(sys.argv[1:])
