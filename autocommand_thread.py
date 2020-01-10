# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:14:41 2019

@author: Wade
"""

import serial
import time
import tkinter
import re
#import pyautogui
import threading
from datetime import datetime
#import time


def autoPVR_Test():
	loop_num = 0
	loop_times = 120
	#prefix_file = "0520G_"
	attach_time_second = 10
	
	#Get timestamp
	now = datetime.now() # current date and time
	date_time = now.strftime("%m%d%H%M%S")
	prefix_file = date_time
	
	#PVR initialization
	autoCommand("\n",1,5)
	autoCommand("df -h",1,5)
	autoCommand("echo 8 > /proc/sys/kernel/printk",1,5)    	
	autoCommand("aui_test",1,2)
	autoCommand("pvr",1,2)
	autoCommand("init",1,5)
	autoCommand("attach /mnt/usb/sda1",1,attach_time_second)
	autoCommand("config encrypt",1,5)
	autoCommand("root",1,2)
	
	while(True):
	#for item in range(12):
		print("loop_num ="+str(loop_num)+"\n")
		autoCommand("\n",1,5)
		autoCommand("stream",1,2)
#		autoCommand("play 0,1,47400,6875,3045,3545,3045,1,0,0",1,10)
#		autoCommand("play 0,1,47400,6875,851,852,851,1,3,0",1,10)
#		autoCommand("play 0,1,47400,6875,831,832,831,1,3,0",1,10)
		autoCommand("play 0,1,47400,6875,3062,3562,3062,1,0,0",1,10)          
		autoCommand("root",1,2)
		autoCommand("pvr",1,2)
#		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,3045,1,1,3545,0,3045,5",1,6)
#		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,851,1,1,852,3,851,5",1,6)   
#		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,831,1,1,832,3,831,5",1,6)   
		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,3062,1,1,3562,0,3062,5",1,6)
		Log.SaveEvent("PVR record")
#		time.sleep(1)
#		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,3062,1,1,3562,0,3062,5",1,6)  
		autoCommand("t",loop_times,60)	#test record
#		autoCommand("t",1,20)        
		autoCommand("s",1,2)
		autoCommand("root",1,2)
		autoCommand("stream",1,2)
		autoCommand("stop",1,2)
		autoCommand("root",1,2)
		autoCommand("pvr",1,2)
		autoCommand("play 0,/mnt/usb/sda1/ALIDVRS2/"+str(prefix_file)+""+str(loop_num),1,2)
		Log.SaveEvent("PVR Playback")
#		autoCommand("play 0,/mnt/usb/sda1/ALIDVRS2/06031132150",1,2)   
		autoCommand("t",loop_times,60)	#test playback
		autoCommand("s",1,5)
		autoCommand("root",1,2)
		loop_num = loop_num + 1

	autoCommand("root",1,2)
	autoCommand("quit",1,2)
    
def autoFullDisk_Test():
    loop_num = 0
    loop_times = 240
	#prefix_file = "0520G_"
    attach_time_second = 12
	
	#Get timestamp
    now = datetime.now() # current date and time
    date_time = now.strftime("%m%d%H%M%S")
    prefix_file = date_time
	
	#PVR initialization
    autoCommand("\n",1,5)
    autoCommand("df -h",1,5)
    autoCommand("echo 8 > /proc/sys/kernel/printk",1,5)    	
	
    while(True):
        print("loop_num begin ="+str(loop_num)+"\n")
        Log.SaveEvent("loop_num begin ="+str(loop_num)+"\n")
        autoCommand("aui_test",1,2)
        autoCommand("root",1,2)
        autoCommand("\n",1,5)
        autoCommand("stream",1,2)
#		autoCommand("play 0,1,47400,6875,3045,3545,3045,1,0,0",1,10)
        autoCommand("play 0,1,47400,6875,851,852,851,1,3,0",1,10)
#		autoCommand("play 0,1,47400,6875,831,832,831,1,3,0",1,10)
#		autoCommand("play 0,1,47400,6875,3062,3562,3062,1,0,0",1,10)            
        autoCommand("root",1,2)
        autoCommand("pvr",1,2)
        autoCommand("init",1,5)
        autoCommand("attach /mnt/usb/sda1",1,attach_time_second)
        autoCommand("config encrypt",1,5)
#		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,3045,1,1,3545,0,3045,5",1,6)
        autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,851,1,1,852,3,851,5",1,6)
        autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,851,1,1,852,3,851,5",1,6)  
#		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,831,1,1,832,3,831,5",1,6)   
#		autoCommand("record "+str(prefix_file)+""+str(loop_num)+",1,3062,1,1,3562,0,3062,5",1,6)
        autoCommand("t",1,1)	#test record
        autoCommand("d",loop_times,60)	#test record            		
        autoCommand("s",1,1)	#test record
        autoCommand("deinit",1,2)	#test record
        autoCommand("root",1,2)
        autoCommand("quit",1,2)
        autoCommand("df -h",1,2)
#        autoCommand("rm /mnt/usb/sda1/* -rf",1,10)
#        autoCommand("sync",1,6)
#        autoCommand("df -h",1,2)
        print("loop_num end ="+str(loop_num)+"\n")
        Log.SaveEvent("loop_num end ="+str(loop_num)+"\n")
        loop_num = loop_num + 1

def autoCommand(command, times, sec_delay):
    for item in range(times):
#		pyautogui.typewrite(command+'\n')
        Console.Write(command)
        time.sleep(sec_delay)

def ShowDialog(message):
    form = tkinter.Tk()
    form.title("Popup Notification")
    form.geometry("300x200")
    lbl = tkinter.Label(form, text=message)
    lbl.pack()
    form.mainloop()

class Console():
    ser = None
    port = "COM3"
    baudrate =115200
    @staticmethod
    def Set(port, baudrate):
        Console.port = port
        Console.baudrate = baudrate
    @staticmethod
    def Initialize():
        if(Console.ser == None):
            Console.ser = serial.Serial(port = Console.port, baudrate = Console.baudrate, bytesize=8,  stopbits=1, parity='N',timeout = 1)
        if(Console.ser.is_open == False):
            Console.ser = serial.Serial(port = Console.port, baudrate = Console.baudrate, bytesize=8,  stopbits=1, parity='N',timeout = 1)       
    @staticmethod
    def Terminate():
        if(Console.ser.is_open == True):        
            Console.ser.close()
    @staticmethod
    def Write(command):
        if(Console.ser.is_open == True):
            command = command+'\n'
            Console.ser.write(command.encode('big5'))
    @staticmethod
    def Read():
        if(Console.ser.is_open == True):
            return Console.ser.readline().decode('big5')
    @staticmethod
    def IsOpen():
        return Console.ser.is_open
    @staticmethod
    def IsWaiting():
        return Console.ser.in_waiting
    
class Log():
    now = None
    date_time = ''
    log_name = ''
    event_name = ''
    fd_log = None
    fd_event = None
    @staticmethod
    def Setup():
        Log.now = datetime.now()
        Log.date_time = Log.now.strftime("%m%d%H%M%S")
        Log.log_name = Log.date_time+".log"
        Log.event_name = Log.date_time+"_event.log"
        Log.fd_log = open(Log.log_name, "w")
        Log.fd_event = open(Log.event_name, "w")
    @staticmethod
    def Logging(message):
        print(message, end='')
        Log.now = datetime.now()
        Log.date_time = Log.now.strftime("%Y/%m/%d,%H:%M:%S:")
        message = Log.date_time + message
        Log.fd_log.write(message)
        Log.fd_log.flush()
    @staticmethod
    def SaveEvent(message):
        Log.now = datetime.now()
        Log.date_time = Log.now.strftime("%Y/%m/%d,%H:%M:%S:")
        message = Log.date_time + message
        # Show a dialog to notif
        threading.Thread(target=ShowDialog,args=(message,)).start()
        Log.fd_event.write(message)
        Log.fd_event.flush()
def main():
    # Setup the serial    
    Console.Initialize()
    if(Console.IsOpen() == False):
        print("Console is not openned yet")
    # Log (print and save log file)
    Log.Setup()
    # Create a thread to run auto test
    test_thread = threading.Thread(target = autoPVR_Test)
#    test_thread = threading.Thread(target = autoFullDisk_Test)
    test_thread_started = False
    re_bootdone = re.compile('File exists')
#    re_stopevent = re.compile('Wade')
    re_fulldiskevent = re.compile('PVR_END_DISKFULL')
    re_loopnum = re.compile('loop_num')
    re_recordfail = re.compile('...........FAIL')
    
    
    while(True):
        if(Console.IsWaiting()):
            line = Console.Read()
            Log.Logging(line)
#            if(re_stopevent.search(line)):
#                Log.SaveEvent(line
            if(re_recordfail.search(line)):
                Log.SaveEvent(line)
            if(re_fulldiskevent.search(line)):
                Log.SaveEvent(line)
                autoCommand("s",1,1)
            if(re_loopnum.search(line)):
                Log.SaveEvent(line)            
#            # Start a thread to run auto test
            if(re_bootdone.search(line)):
                if(test_thread_started==False):
                    print("############## Start test_thread: #############")
                    test_thread.start()
                    test_thread_started = True
    Console.Terminate()
        
if __name__ == '__main__':
    main()
