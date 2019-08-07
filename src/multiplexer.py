#!/usr/bin/python
# from John Wood at bitbucket.org/kolon/my-pi-projects/
import smbus

class multiplex:
    
    def __init__(self, bus):
        self.bus = smbus.SMBus(bus)

    def channel(self, address=0x70,channel=0):  # values 0-7 indicate the channel, anything else (eg -1) turns off all channels
        
        if   (channel==0): action = 0x01
        elif (channel==1): action = 0x02
        elif (channel==2): action = 0x03
        elif (channel==3): action = 0x04
	elif (channel==4): action = 0x05
        elif (channel==5): action = 0x06
        elif (channel==6): action = 0x07
        elif (channel==7): action = 0x08
        else : action = 0x00

        self.bus.read_byte_data(address,0x04,action)  #0x04 is the register for switching channels 

if __name__ == '__main__':
    
    bus=1       # 0 for rev1 boards etc.
    address=0x70
    
    plexer = multiplex(bus)
    plexer.channel(address,3)
    
    print "Now run i2cdetect"




