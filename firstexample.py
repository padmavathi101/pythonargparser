#!/usr/bin/python
import argparse,subprocess


def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    group.add_argument("--verbose","-v",help="increase output verbosity",action="store_true")
    group.add_argument("--quiet","-q",help="quietly display",action="store_true")
    parser.add_argument("--ip_addr",help="give the input of the ip address",type=str,required=True)
    parser.add_argument("--port_no",help="give the input of the port no",type=int)
    args=parser.parse_args()
    #print parser.print_help()
    if args.ip_addr:
        print("ip addr is "+str(args.ip_addr))
    if args.port_no:
        print("port no is "+str(args.port_no))
    else:
        print("all port numbers")
    if args.verbose:
        print"selected verbose"
    if args.quiet:
        print"selected quiet"
    print subprocess.check_output(["/usr/bin/nmap","-p",str(args.port_no),str(args.ip_addr)])
    print subprocess.check_output(["/bin/ping","-c","5",str(args.ip_addr)])
if __name__=="__main__":
    main()
