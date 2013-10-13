#-------------------------------------------------------------------------------
# Name:        Game Bot
# Purpose:
#
# Author:      LIC
#
# Created:     13-10-2013
# Copyright:   (c) LIC 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import ImageGrab
import os #to get cwd
import time #for timestamp

x_pad = 199
y_pad = 181

"""
All coordinates assume a screen resolution of 1366x768, and Chrome
maximized with the Bookmarks Toolbar disabled.
1 Scroll is used to center play area in browser.
x_pad = 199
y_pad = 181
Play area =  x_pad+1, y_pad+1, x_pad + 640,y_pad+479
"""
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad + 640,y_pad+479) #Tuple
    im = ImageGrab.grab(box)   #it return rgb image to im

    #Save function requires location and format
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()