#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:07:29 2020

@author: pi
"""

# =============================================================================
# Header file for interfacing i2c controlled 16x2 display
# Need to be included for controlling the display
# Connect SDC to GPIO 2 and SCL to GPIO 3 which is I2C 1 iterface of RPi
# =============================================================================
import I2C_LCD_driver
import time


# =============================================================================
# Assigning all the functions under class lcd to the pointer mylcd
# =============================================================================
mylcd = I2C_LCD_driver.lcd()


# =============================================================================
# Printing a simple string on the display
#("String to be printed",row number(1,2), column number (0-15))
# =============================================================================
#mylcd.lcd_display_string("a",1,0)
#time.sleep(5)


# =============================================================================
# Command to clear the display
# =============================================================================

mylcd.lcd_clear()

# =============================================================================
# Printing the date and time format
# =============================================================================
#
mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)


time.sleep(3)
mylcd.lcd_clear()

# =============================================================================
# Macro to scroll the text from left to right once
# =============================================================================
str_pad = " " * 16
my_long_string = "This is a long string that needs to be dislayed!"
my_long_string = str_pad + my_long_string

for i in range (0, len(my_long_string)):
    lcd_text = my_long_string[i:(i+16)]
    mylcd.lcd_display_string(lcd_text,1)
    time.sleep(0.4)
    mylcd.lcd_display_string(str_pad,1)

# =============================================================================
# Macro to scroll text from right to left once
# =============================================================================
#padding = " " * 16
#my_long_string = "To be or not to be that is the question!"
#padded_string = padding+ my_long_string + padding
#
#for i in range (0, len(my_long_string)):
# lcd_text = padded_string[((len(my_long_string)-1)-i):-i]
# mylcd.lcd_display_string(lcd_text,1)
# time.sleep(0.4)
# mylcd.lcd_display_string(padding[(15+i):i], 1)
# 
time.sleep(3)
mylcd.lcd_clear()
# =============================================================================
# Macro for special characters
# =============================================================================
#write pixel values for 5x8 grid
fontdata1 = [      
        [ 0b00010, 
          0b00100, 
          0b01000, 
          0b10000, 
          0b01000, 
          0b00100, 
          0b00010, 
          0b00000 ],
        [ 0b11111,
          0b10001,
          0b10001,
          0b10001,
          0b10001,
          0b10001,
          0b10001,
          0b11111,]
]

mylcd.lcd_load_custom_chars(fontdata1)
mylcd.lcd_write(0xC0)
mylcd.lcd_write_char(0)

mylcd.lcd_write(0x80)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(0)

# =============================================================================
# Macro for printing right pointing arrow on the left of LCD
# =============================================================================

#fontdata1 = [
#        # char(0) - Upper-left character
#        [ 0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b11111, 
#          0b11111 ],
#
#        # char(1) - Upper-middle character
#        [ 0b00000, 
#          0b00000, 
#          0b00100, 
#          0b00110, 
#          0b00111, 
#          0b00111, 
#          0b11111, 
#          0b11111 ],
#        
#        # char(2) - Upper-right character
#        [ 0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b10000, 
#          0b11000 ],
#        
#        # char(3) - Lower-left character
#        [ 0b11111, 
#          0b11111, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000 ],
#       
#        # char(4) - Lower-middle character
#        [ 0b11111, 
#          0b11111, 
#          0b00111, 
#          0b00111, 
#          0b00110, 
#          0b00100, 
#          0b00000, 
#          0b00000 ],
#        
#        # char(5) - Lower-right character
#        [ 0b11000, 
#          0b10000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000, 
#          0b00000 ],
#]
#
#mylcd.lcd_load_custom_chars(fontdata1)
#
#mylcd.lcd_write(0x80)
#mylcd.lcd_write_char(0)
#mylcd.lcd_write_char(1)
#mylcd.lcd_write_char(2)
#
#mylcd.lcd_write(0xC0)
#mylcd.lcd_write_char(3)
#mylcd.lcd_write_char(4)
#mylcd.lcd_write_char(5)