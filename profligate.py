#!/usr/bin/python

import time
#import unittest

def search():
#Find the RRD files 
    pass

def trim():
# Select recently updated files and cover memory and CPU.
    pass

def average():
# Find the average of RRD file values.
    pass

def trigger():
# Keep a list of servers that need reporting. 
    pass

def unfloat(UnixTime, FloatString):
# Convert memory values to a human readable format.
    FloatPower = int(FloatString[14:16])
    FloatValue = float(FloatString[0:-5])*(10**FloatPower)
    UnixTime = UnixTime[0:9]
    
    
    #vol-e17997e7
    
    if FloatPower > 14:
        FloatValue = FloatValue / (1024**5)
        ScaleText = "Pb"
    elif FloatPower > 11:
        FloatValue = FloatValue / (1024**4)
        ScaleText = "Tb"
    elif FloatPower > 8:
        FloatValue = FloatValue / (1024**3)
        ScaleText = "Gb"
    elif FloatPower > 5:
        FloatValue = FloatValue / (1024**2)
        ScaleText = "Mb"
    elif FloatPower > 2:
        FloatValue = FloatValue / 1024
        ScaleText = "Kb"
    else:
        ScaleText = "bytes"
    
    
    
    if FloatPower in [3,6,9,12,15]:
        Output = str(round(FloatValue, 1)) + ScaleText
    else:
        Output = str(int(FloatValue)) + ScaleText
        
    #print Output
    #print SimpleDate(UnixTime, tz='utc').date
    return Output

def sendemail():
# Send an email.
    pass

def writehtml():
# Write a html report.
    pass
