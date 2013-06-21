from random import randint
import re,os,sys

try:
    interface = sys.argv[1]
except IndexError:
    print 'Usage: python ' + sys.argv[0] + ' <interface>'
    sys.exit(0)

myRegex = '0x([\w\d]{2})'

t00 =  hex(randint(16,255))
t10 =  hex(randint(16,255))
t20 =  hex(randint(16,255))
t30 =  hex(randint(16,255))
t40 =  hex(randint(16,255))
t50 =  hex(randint(16,255))

m0 = re.match(myRegex,t00)
m1 = re.match(myRegex,t10)
m2 = re.match(myRegex,t20)
m3 = re.match(myRegex,t30)
m4 = re.match(myRegex,t30)
m5 = re.match(myRegex,t50)

t0 = m0.group(1)
t1 = m1.group(1)
t2 = m2.group(1)
t3 = m3.group(1)
t4 = m4.group(1)
t5 = m5.group(1)

myMac = t0 + ':' + t1 + ':' + t2 + ':' + t3 + ':' + t4 + ':' + t5

os.system('sudo ip link set dev ' + interface  + ' down')
os.system('sudo ip link set dev ' + interface  + ' address ' + myMac)
os.system('sudo ip link set dev ' + interface  + ' up')
