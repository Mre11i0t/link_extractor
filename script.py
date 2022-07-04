# Command to run on each url 
# ./linkextract -s -r 1 https://{domain}
# if error fallback to ./linkExtract -s -r 1 http://{domain}/

# Take path as argument
import argparse
import os
flag_list = ["ajax.googleapis.com","maxcdn.bootstrapcdn.com","policies.google.com","www.gstatic.com","cdn","unkpkg.com"]
arg=argparse.ArgumentParser()
arg.add_argument("-t","--target",help="Target domain file list")
arg.add_argument("-o","--output",help="Output file")
# Get arguments
args=arg.parse_args()
# Create a output file if not exist
if not os.path.isfile(args.output):
    open(args.output,"w").close()
# Open output file
out=open(args.output,"a")
# Open file and read lines
with open(args.target) as f:
    lines = f.readlines()
# For each line
for line in lines:
    try:
        os.system("./linkExtract -s -r 1 https://"+line.strip()+"/ > url.txt")
    except:
        os.system("./linkExtract -s -r 1 http://"+line.strip()+"/ > url.txt")
    # Open url.txt and read lines
    with open("url.txt") as uf:
        urls = uf.readlines()
    for urlline in urls:
        x = urlline.strip()
        if line.strip() not in urlline.strip():
            # Check if domain is in flag list
            if any(flag in x for flag in flag_list):
                continue
            out.write(line.strip()+","+urlline.strip()+"\n")
    uf.close()
    os.system("rm url.txt")
out.close() 