from array import *
import random
import sys
import csv


SPEEDPICKUP = []
SPEEDDROPOFF = []
PICKUP = []
DROPOFF = [] 


with open('ToolPostCoords.csv', newline='') as csvfile:
    coordreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in coordreader:
        if row[0].isdigit():
            #Parse Pickup and Dropoff Coordinates
            PICKUP.append(row[2:9])
            DROPOFF.append(row[10:18])
        if row[0] == 'Speed (F):':
            #Parse Pickup and Dropoff Speed
            SPEEDPICKUP = row[2:9]
            SPEEDDROPOFF = row[10:18]

"""
TOOL1PICKUP = [143.5, 9, 50, 0, 158.5, 50, 160]
TOOL2PICKUP = [143.5, 53, 0, 0, 158.5, 50, 160]
TOOL3PICKUP = [143.5, 108, 50, 0, 158.5, 50, 160]
TOOL4PICKUP = [143.5, 144, 50, 0, 158.5, 50, 160]
TOOL5PICKUP = [143.5, 189, 50, 0, 158.5, 50, 160]
TOOL6PICKUP = [143.5, 234, 50, 0, 158.5, 50, 160]
TOOL7PICKUP = [143.5, 280, 50, 0, 158.5, 50, 160]
TOOL8PICKUP = [143.5, 324, 50, 0, 158.5, 50, 160]
TOOL9PICKUP = [143.5, 367, 50, 0, 158.5, 50, 160]
TOOL10PICKUP = [3.5, 10, 70, 39, 18.5, 70, 15]
TOOL11PICKUP = [3.5, 54, 70, 39, 18.5, 70, 15]
TOOL12PICKUP = [3.5, 100, 70, 39, 18.5, 70, 15]
TOOL13PICKUP = [3.5, 144, 70, 39, 18.5, 70, 15]
TOOL14PICKUP = [3.5, 190, 70, 39, 18.5, 70, 15]
TOOL15PICKUP = [3.5, 234, 70, 39, 18.5, 70, 15]
TOOL16PICKUP = [3.5, 279, 70, 39, 18.5, 70, 15]
TOOL17PICKUP = [3.5, 325, 70, 39, 18.5, 70, 15]
TOOL18PICKUP = [3.5, 367, 70, 39, 18.5, 70, 15]

TOOL1DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL2DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL3DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL4DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL5DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL6DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL7DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL8DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL9DROPOFF = [160, 9, 50, 158.5, 0, 143.5, 70, 160]
TOOL10DROPOFF = [15, 10, 70, 18.5, 39, 3.5, 70, 15]
TOOL11DROPOFF = [15, 54, 70, 18.5, 39, 3.5, 70, 15]
TOOL12DROPOFF = [15, 100, 70, 18.5, 39, 3.5, 70, 15]
TOOL13DROPOFF = [15, 144, 70, 18.5, 39, 3.5, 70, 15]
TOOL14DROPOFF = [15, 190, 70, 18.5, 39, 3.5, 70, 15]
TOOL15DROPOFF = [15, 234, 70, 18.5, 39, 3.5, 70, 15]
TOOL16DROPOFF = [15, 279, 70, 18.5, 39, 3.5, 70, 15]
TOOL17DROPOFF = [15, 325, 70, 18.5, 39, 3.5, 70, 15]
TOOL18DROPOFF = [15, 367, 70, 18.5, 39, 3.5, 70, 15]

SPEEDPICKUP = [500, 500, 500, 200, 200, 200, 500]
SPEEDDROPOFF = [500, 500, 500, 500, 200, 200, 500, 500]

PICKUP = [TOOL1PICKUP, TOOL2PICKUP, TOOL3PICKUP, TOOL4PICKUP, TOOL5PICKUP, TOOL6PICKUP, TOOL7PICKUP, TOOL8PICKUP, TOOL9PICKUP, TOOL10PICKUP, TOOL11PICKUP, TOOL12PICKUP, TOOL13PICKUP, TOOL14PICKUP, TOOL15PICKUP, TOOL16PICKUP, TOOL17PICKUP, TOOL18PICKUP]

DROPOFF = [TOOL1DROPOFF, TOOL2DROPOFF, TOOL3DROPOFF, TOOL4DROPOFF, TOOL5DROPOFF, TOOL6DROPOFF, TOOL7DROPOFF, TOOL8DROPOFF, TOOL9DROPOFF, TOOL10DROPOFF, TOOL11DROPOFF, TOOL12DROPOFF, TOOL13DROPOFF, TOOL14DROPOFF, TOOL15DROPOFF, TOOL16DROPOFF, TOOL17DROPOFF, TOOL18DROPOFF] 
"""
ran = random.randint(0,len(PICKUP)-1)

#Default values
fname = "tooltest.gcode"
toolchange = 10

#if user provided arguments
if len(sys.argv) > 3:
    print("usage: gcode_gen.py [optional: number of toolchanges (= 10)] [optional: filename (= tooltest.gcode)]")
    exit()
elif len(sys.argv) == 3:
    toolchange = int(sys.argv[1])
    fname = sys.argv[2]
elif len(sys.argv) == 2:
    toolchange = int(sys.argv[1])


print("Generating from ToolPostCoords.csv with", toolchange, "tool changes.")


#First few lines
f = open(fname, "w")
f.write("G28 ; home all axes\n")
f.write("G21 ; set units to millimeters\n")
f.write("G90 ; use absolute coordinates\n")
f.write("G92 U0 ; reset extrusion distance\n")


for x in range(toolchange):
 #Pickup tool
 f.write("\n")
 f.write("G01 Z"+str(PICKUP[ran][0])+" F"+str(SPEEDPICKUP[0])+"; move towards tool post\n")
 f.write("G01 X"+str(PICKUP[ran][1])+" Y"+str(PICKUP[ran][2])+" F"+str(SPEEDPICKUP[1])+"; get near tool post " + str(ran)+"\n")
 f.write("G01 Y"+str(PICKUP[ran][3])+" F"+str(SPEEDPICKUP[2])+"; engage magnets with new tool\n")
 f.write("G01 Z"+str(PICKUP[ran][4])+" F"+str(SPEEDPICKUP[3])+"; move upward and pull tool off of post\n")
 f.write("G01 Y"+str(PICKUP[ran][5])+" F"+str(SPEEDPICKUP[4])+"; move away from tool post with new tool\n")
 f.write("G01 Z"+str(PICKUP[ran][4])+" F"+str(SPEEDPICKUP[4])+"; force upward movement to ensure there's no contact with walls\n")

 f.write("\n")

 #Dropoff Tool
 f.write("G01 Z"+str(DROPOFF[ran][0])+" F"+str(SPEEDDROPOFF[0])+"; retract z to some high position\n")
 f.write("G01 X"+str(DROPOFF[ran][1])+" Y"+str(DROPOFF[ran][2])+" F"+str(SPEEDDROPOFF[1])+"; get in front of proper tool post\n")
 f.write("G01 Z"+str(DROPOFF[ran][3])+" F"+str(SPEEDDROPOFF[3])+"; set the correct z height in front of tool post " + str(ran)+"\n")
 f.write("G01 Y"+str(DROPOFF[ran][4])+" F"+str(SPEEDDROPOFF[4])+"; move towards tool post\n")
 f.write("G01 Z"+str(DROPOFF[ran][5])+" F"+str(SPEEDDROPOFF[5])+"; move down and place tool onto tool post\n")
 f.write("G01 Y"+str(DROPOFF[ran][6])+" F"+str(SPEEDDROPOFF[6])+"; return to safe distance without tool (move back)\n")
 f.write("G01 Z"+str(DROPOFF[ran][7])+" F"+str(SPEEDDROPOFF[7])+"; move to z to a high position (move up)\n")
 
 
 ran = random.randint(0,len(PICKUP)-1)

#Home printer head 
f.write("\n")
f.write("G28 U ; home extrusion (u) axis\n")
f.write("G28 Z ; home z axis\n")
f.write("G28 X Y ; home x and y axes\n")
f.close()

print("DONE: Output is at", fname)
