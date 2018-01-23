#!/usr/bin/env python

def showMainMenu():
	ans=True
	while ans:
		print ("""
		1. Setup new node
		2. Update node
		3. Option 3
		4.Exit/Quit
		""")
		ans=raw_input("What would you like to do? \n") 
		if ans=="1": 
			print("\n OK, let's setup new node")
			## show menu for node setup
			showSetupNodeMenu()
		elif ans=="2":
			print("\n OK, let's update a node")
			## show menu for node update
			showUpdateNodeMenu()
		elif ans=="3":
			print("\n Option 3")
			## show menu for option 3
		elif ans=="4":
			print("\n Goodbye") 
			exit()
		elif ans !="":
			print("\n Not a valid choice. Try again") 

def showSetupNodeMenu():
	ans=True
	while ans:
		print ("""
		1. Core
		2. Sokol
		3.Exit/Quit
		""")
		ans=raw_input("Which network?") 
		if ans=="1": 
			print("\n OK, let's deploy new node on Core")
			networkType = "core"
			## show submenu
			showSetupNodeMenu_1()
		elif ans=="2":
			print("\n OK, let's deploy new node on Sokol")
			networkType = "sokol"
			## show submenu
			showSetupNodeMenu_1()
		elif ans=="3":
			print("\n Goodbye")
			exit()
		elif ans !="":
			print("\n Not a valid choice. Try again") 
			
def showSetupNodeMenu_1():
	ans=True
	while ans:
		print ("""
		1. bootnode
		2. validator
		3. Master of Ceremony (MoC)
		4. Exit/Quit
		""")
		ans=raw_input("...?") 
		if ans=="1": 
			print("\n OK, let's deploy bootnode")
			## show menu for node setup
		elif ans=="2":
			print("\n OK, let's deploy validator node")
			## show menu for node update
		elif ans=="3":
			print("\n OK, let's deploy Master of Ceremony node")
		elif ans=="4":
			print("\n Goodbye")
			exit()
		elif ans !="":
			print("\n What type of node? \n") 

def showUpdateNodeMenu():
	ans=True
	while ans:
		print ("""
		1. 1
		2. 2
		3. 3
		4.Exit/Quit
		""")
		ans=raw_input("...?") 
		if ans=="1": 
			print("\n 1")
			## show menu for node setup
		elif ans=="2":
			print("\n 2")
			## show menu for node update
		elif ans=="3":
			print("\n 3")
			## show menu for option 3
		elif ans=="4":
			print("\n Goodbye")
			exit()
		elif ans !="":
			print("\n Not a valid choice. Try again \n")
			
			
			
			
showMainMenu()
