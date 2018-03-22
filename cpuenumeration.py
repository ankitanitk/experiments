import os
import sys
import subprocess
import re
from itertools import izip



var = subprocess.check_output("cat /proc/cpuinfo",shell=True)
#print var
f= open('output1.txt','w')
f.write(var)

a=subprocess.check_output(" cat /etc/issue",shell=True)
a= str(a)
#print a
if a.find("SUSE")== -1:
	subprocess.check_output(" yum install -y acpica-tools",shell=True)
else:
	subprocess.check_output(" zypper install -y acpica",shell=True)

os.system(" acpidump > acpi.dat")

os.system(" acpixtract -a acpi.dat")

os.system(" iasl -d apic.dat")

d=subprocess.check_output(" cat apic.dsl",shell=True)

f1=open('output2.txt','w')
f1.write(d)

f2= open('cpuinfo','w')
for line in open('output1.txt'):
    if line.startswith('apicid'):
      # print line
       line= line[10:]
       f2.write(line)


f3= open('apicfile','w')
with open("output2.txt") as f:
    for line in f:
        if "Local Apic ID" in line:
                #m= re.compile('Local(.*?)ID',re.DOTALL | re.IGNORECASE).findall(line).strip()
                #print m
                line=line[47:]
                i= int(line,16)
                i=str(i)+ "\n"
                f3.write(i)



f4= open('trial.txt','w')
with open('apicfile') as as1, open('cpuinfo') as as2:
        for x,y in izip(as1,as2):
                x=x.strip()
                y=y.strip()
                a= x==y
                if a=='False':
                        print ("FAIL")
                        break
                #print("{0}\t{1}\t{2}".format(x, y ,a))

print ("PASS")









