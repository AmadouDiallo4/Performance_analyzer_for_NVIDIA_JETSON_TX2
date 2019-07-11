#Author : Siddharth Menon (Written by reffering matplotlib documentation)
#Code specific to NVIDIA Jetson TX2
import sys 
import os
import json
import threading
from collections import deque
import time

import numpy as np
import statistics  
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Remove all unnnessory/ commented lines



class Benchmarking:
	t1 = threading.Thread
	start=False
	temporary_file = open("temporary_file.txt", "w+")
	
	def start_recording(self):
		self.t1 = threading.Thread(target=self.model_report) 
		self.t1.start()
		self.start = True
		
	def stop_recording(self):
		self.start = False
		self.t1.join()
 
	def model_report(self):
                # do group initialisation
		gpu_list,cpu_list,cpu_list1,gpu_temp,cpu_temp,timer,list1,power_consumption_list=[]
		
		def gpu_usage():

                # Adopt one convention: Camel case or underscore
                # Don't use numeric constants. Use variables
                # Example: scale_down_factor = 10
			scale_down_factor_for_gpu=10
			gpu_Load_File="/sys/devices/gpu.0/load"
			with open(gpu_Load_File, 'r') as gpu_File:
				gpuusage=gpu_File.read()
			gpu_value=float(gpuusage)/scale_down_factor_for_gpu
			return gpu_value

		def cpu_usage():

                # Try to use two spaces instead of four spaces

		# Example: bad code: cpu_free=((8-((float(line[17])*10 + float(line[18]))/10))/8)*100
                
                # Example: good code:  Try with reduce, map and simplify this logic
			
			cpuLoadFile="/proc/meminfo"

			with open(cpuLoadFile) as fp:
				for i, line in enumerate(fp):
					if i == 2:
						cpu_free=((8-((float(line[17])*10 + float(line[18]))/10))/8)*100
						break
			return cpu_free
			
		def gpu_temperature():
			
			tempLoadFile="/sys/devices/virtual/thermal/thermal_zone2/temp"
			scale_down_factor_for_temp=1000
			with open(tempLoadFile,'r') as tempFile:
				temp=tempFile.read()
			gpu_temp_value=float(temp)/scale_down_factor_for_temp
			return gpu_temp_value

		def cpu_temperature():
			
			tempLoadFile1="/sys/devices/virtual/thermal/thermal_zone1/temp"

			with open(tempLoadFile1,'r') as tempFile1:
				temp1=tempFile1.read()
			cpu_temp_value=float(temp1)/scale_down_factor_for_temp
			return cpu_temp_value
			
		def power_consumption():
			
			tempLoadFile2="/sys/bus/i2c/drivers/ina3221x/0-0041/iio_device/in_power0_input"

			with open(tempLoadFile2,'r') as tempFile2:
				temp2=tempFile2.read()
			power_value=float(temp2)
			return power_value
			
			
		while(True):
			if(self.start==True):
				break

                # Don't exceed 100 characters in line
                # Split longeer lines into shorter lines
			
		start_time=time.time()	
		with open('temporary_file.txt', 'w+') as temporary_file_write:
			while (self.start):
				temporary_file_write.write("%f\n%f\n%f\n%f\n%f\n"%
                                        (gpu_usage(),cpu_usage(),gpu_temperature(),
                                            cpu_temperature(),power_consumption()))
				timer.append(time.time()-start_time)
			
		file= open("temporary_file.txt","r") 
		list1 = []
		value1=file.readlines()
		for value in value1:
			value=float(value)
			list1.append(value)
          
                # use string operations to simplify this logic 
		gpu_list=list1[0::5]
		cpu_list=list1[1::5]
		gpu_temp=list1[2::5]
		cpu_temp=list1[3::5]
		power_consumption_list=list1[4::5]	

                # Remove all print statements
                 
                # Put this code into a function. Pass in sub plot index
                # label names. Nice to have. not must have

		plt.subplot(3, 1, 1)
		plt.plot(timer, gpu_list,label='GPU Usage')
		plt.plot(timer, cpu_list,label='RAM')	
		plt.title('Model Inference Report')
		plt.ylabel('Usage (%)')
		plt.title('AVG GPU usage: %f , Avg RAM Used: %f'%(statistics.mean(gpu_list),statistics.mean(cpu_list)))
		plt.legend()
		
		plt.show()
		plt.subplot(3, 1, 2)
		plt.plot(timer, gpu_temp,label='GPU Temp')
		plt.plot(timer,cpu_temp,label='CPU Temp')
		
		plt.ylabel('Temperature')
		plt.title('Avg GPU temp: %f , Avg CPU Temp: %f'%(statistics.mean(cpu_temp),statistics.mean(gpu_temp)))
		plt.legend()
		
		plt.show()
		plt.subplot(3,1,3)
		plt.plot(timer,power_consumption_list)
		plt.xlabel('time(s)')
		plt.ylabel('Power_consumption')
		plt.title('AVG Power consumed in: %f milliWatts'%statistics.mean(power_consumption_list))
		plt.subplots_adjust(left=None, bottom=None, right=1, top=None, wspace=None, hspace=1)

			
		plt.savefig('./model.png')

# Have a better name. Choose decrptive variable names that convey the 
# intent of the variable
		
analyzer = Benchmarking()

