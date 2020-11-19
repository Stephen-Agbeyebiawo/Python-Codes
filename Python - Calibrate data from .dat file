# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:30:46 2020

@author: Stephen Agbeyebiawo
"""

filename = "SensorData.dat"
newList = []

#open SensorData file and read each line into a list
with open(filename) as fn:
    content = fn.readlines()
    
#remove new line characters from end of each list entry 
content = [x.strip() for x in content]

#loop through the list to calibrate the values
for i in range(len(content)):
    datatype = content[i].split(',')[0]
    value = float(content[i].split(',')[1])
    if datatype == 'A':
        value = 0.95 * value + 0.2
    elif datatype == 'X':
        value = 1.01 * value + 0.3
    elif datatype == 'R':
        value = value
    newList.append(datatype + "," + str(value))
print('Calibrated Data is ', newList)

#create new file "CalibratedSensorData.dat" to save calibrated data
newFile = 'CalibratedSensorData.dat'
with open(newFile,'w') as fn:
    fn.writelines("%s\n"  % newValue for newValue in newList)
