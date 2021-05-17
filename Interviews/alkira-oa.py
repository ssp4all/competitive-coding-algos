<<<<<<< Updated upstream
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processorTime
#  2. INTEGER_ARRAY taskTime
#

def minTime(processorTime, taskTime):
    # Write your code here
    
    taskTime.sort(reverse=1)
    processorTime.sort()
    
    cur_task, res = 0, 0 
    for time in processorTime:
        for job in range(4):
            cur_time = taskTime[cur_task] + time 
            cur_task += 1 
            res = max(res, cur_time)
            
    return res

if __name__ == '__main__':

##############################################
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'validateAddresses' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY addresses as parameter.
#

import re

def get_ipv4_pattern():
    byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'
    regex = '^{0}(\.{0}){{3}}$'.format(byte)
    pattern = re.compile(regex)
    return pattern 

def get_ipv6_pattern():
    hex = '[0-9A-Fa-f]{1,4}'
    regex = '^({0})(:{0}){{7}}$'.format(hex)
    pattern = re.compile(regex)
    return pattern 
    
def validateAddresses(addresses):
    # Write your code here
    
    valid_ips = []
    n = len(addresses)
    
    ipv4 = get_ipv4_pattern()
    ipv6 = get_ipv6_pattern() 
    
    for address in addresses:
        if ipv4.match(address):
            valid_ips += ['IPv4']
        elif ipv6.match(address):
            valid_ips += ['IPv6']
        else:
            valid_ips += ['Neither']
    
    return valid_ips

=======
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processorTime
#  2. INTEGER_ARRAY taskTime
#

def minTime(processorTime, taskTime):
    # Write your code here
    
    taskTime.sort(reverse=1)
    processorTime.sort()
    
    cur_task, res = 0, 0 
    for time in processorTime:
        for job in range(4):
            cur_time = taskTime[cur_task] + time 
            cur_task += 1 
            res = max(res, cur_time)
            
    return res

if __name__ == '__main__':

##############################################
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'validateAddresses' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY addresses as parameter.
#

import re

def get_ipv4_pattern():
    byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'
    regex = '^{0}(\.{0}){{3}}$'.format(byte)
    pattern = re.compile(regex)
    return pattern 

def get_ipv6_pattern():
    hex = '[0-9A-Fa-f]{1,4}'
    regex = '^({0})(:{0}){{7}}$'.format(hex)
    pattern = re.compile(regex)
    return pattern 
    
def validateAddresses(addresses):
    # Write your code here
    
    valid_ips = []
    n = len(addresses)
    
    ipv4 = get_ipv4_pattern()
    ipv6 = get_ipv6_pattern() 
    
    for address in addresses:
        if ipv4.match(address):
            valid_ips += ['IPv4']
        elif ipv6.match(address):
            valid_ips += ['IPv6']
        else:
            valid_ips += ['Neither']
    
    return valid_ips

>>>>>>> Stashed changes
if __name__ == '__main__':