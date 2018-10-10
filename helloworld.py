# hellworld.py                                                                #
#                                                                             #
# Summary                                                                     #
#                                                                             #
#     This python script demonstrates a simple connection between a Raspberry #
#     Pi and an ADS1115 Analog to Digital converter, writing text to a CSV    #
#     file.                                                                   #  
#                                                                             #  
#     The ADS1115 VDD should be connected to the Raspberry Pi 3.3V, GND to    #
#     GND, SCL to SCL (RPi GPIO 3, pin 5), SDA to SDA (RPi GPIO 2, pin 3).    #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import all necessary libraries
import Adafruit_ADS1x15

# create ADS1115 instance
adc = Adafruit_ADS1x15.ADS1115()

# Set gain - table below explains voltage ranges for different gains
# 2/3 = +/- 6.144V
#   1 = +/- 4.096V
#   2 = +/- 2.048V
#   4 = +/- 1.024V
#   8 = +/- 0.512V
#  16 = +/- 0.256V
# See the ADS1115 datasheet for more info
GAIN = 1

# open file to write to; creates new file or overwrites existing data
csv = open("csvdata.csv", "w")

# read voltages from each channel 5 times, print values to CSV file
for i in range(5): 

    values = [0]*4

    for j in range(4): 

        # read voltages into array
        values[j] = adc.read_adc(j, gain=GAIN)

    # write voltages to CSV file 
    csv.write("%1.2f,%1.2f,%1.2f,%1.2f\n" % (values[0], values[1], values[2],
                                                             values[3]))
              

# close file
csv.close()
