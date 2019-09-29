from tkinter import *
from threading import Thread
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GUI(Thread):
	def __init__(self):
		Thread.__init__(self)
		
		self.m1 = 0
		self.m2 = 0
		self.v1 = 0
		self.v2 = 0
		
	def run(self):
		self.fenster = Tk()
		
		self.fenster.iconbitmap("pics/car_crash_icon.ico")
		
		def calc():
			self.m1 = float(car_mass_entry.get())
			self.m2 = float(animal_mass_entry.get())
			self.v1 = float(speed_entry.get())/3.6
			
			self.v2 = round(((self.v1*self.m1)/(self.m1+self.m2))*3.6, 2)
			energy = round(0.5*self.m1*self.v1**2 ,2)
			
			pathway = round(float(reaction_time_entry.get())*(self.v2*3.6), 2)
			
			way = round(0.5*self.v2*((self.v2+float(Acceleration_entry.get())*float(reaction_time_entry.get()))/float(Acceleration_entry.get())), 2)
			
			result_label = Label(self.fenster, text="Speed after impact: "+str(self.v2)+" km/h\nProduced Energy: "+str(energy)+" J\nPathway: "+str(pathway)+" m\nWay: " + str(way) + "m")
			result_label.grid(row=5, column=0, pady=20, padx=20)
			
			rtime =  str((pathway/(self.v2*3.6)/1000))
			rtime = rtime.split(".")[0]
			print(rtime)
			
			plot = []
			for i in range(0, int(rtime), 1):
				plot.append(i)
			
			df = pd.DataFrame(plot, columns=['Velocity'])

			df.plot()
			plt.show()
		
		self.fenster.title("Car impact calculator")
		
		car_mass_label = Label(self.fenster, text="Mass of the car")
		car_mass_entry = Entry(self.fenster, bd=5, width=20)
		car_mass_label.grid(row=0, column=0, pady=20, padx=20)
		car_mass_entry.grid(row=0, column=1, pady=20, padx=20)
		
		car_unit_label = Label(self.fenster, text="kg")
		car_unit_label.grid(row=0, column=3, pady = 20, padx = 20)
		
		speed_label = Label(self.fenster, text="Speed of the car")
		speed_entry = Entry(self.fenster, bd=5, width = 20)
		speed_label.grid(row=1, column=0, pady=20, padx=20)
		speed_entry.grid(row=1, column=1, pady=20, padx=20)
		
		speed_unit_label = Label(self.fenster, text="km/h")
		speed_unit_label.grid(row=1, column=3, pady = 20, padx = 20)
		
		animal_mass_label = Label(self.fenster, text="Mass of the animal")
		animal_mass_entry = Entry(self.fenster, bd=5, width=20)
		animal_mass_label.grid(row=2, column=0, pady=20, padx=20)
		animal_mass_entry.grid(row=2, column=1, pady=20, padx=20)
		
		animal_unit_label = Label(self.fenster, text="kg")
		animal_unit_label.grid(row=2, column=3, pady = 20, padx = 20)
		
		reaction_time_label = Label(self.fenster, text="Reaction time")
		reaction_time_entry = Entry(self.fenster, bd=5, width=20)
		reaction_time_label.grid(row=3, column=0, pady=20, padx=20)
		reaction_time_entry.grid(row=3, column=1, pady=20, padx=20)
		
		reaction_time_unit_label = Label(self.fenster, text="s")
		reaction_time_unit_label.grid(row=3, column=3, pady = 20, padx = 20)
		
		Acceleration_label = Label(self.fenster, text="Break acceleration")
		Acceleration_entry = Entry(self.fenster, bd=5, width=20)
		Acceleration_label.grid(row=4, column=0, pady=20, padx=20)
		Acceleration_entry.grid(row=4, column=1, pady=20, padx=20)
		
		Acceleration_unit_label = Label(self.fenster, text="m/s^2")
		Acceleration_unit_label.grid(row=4, column=3, pady = 20, padx = 20)
		
		send_data = Button(self.fenster, text="Calculate", command=calc)
		send_data.grid(row=5, column=1, pady=20, padx=20)
		
		self.fenster.mainloop()
		self.fenster.quit()
		
GUI().start()