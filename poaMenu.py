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
			print("\n OK, let's setup new node on Core")
			networkType = "core"
			## show submenu
			showSetupNodeMenu_1()
		elif ans=="2":
			print("\n OK, let's setup new node on Sokol")
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
		4. Go back to the main menu
		5. Exit/Quit
		""")
		ans=raw_input("...?") 
		if ans=="1": 
			print("\n OK, let's setup bootnode")
			## show menu for node setup
			nodeType = 'bootnode'
			collectBootnodeInfo()
		elif ans=="2":
			print("\n OK, let's setup validator node")
			## show menu for node update
			nodeType = 'validator'
			collectValidatorInfo()
		elif ans=="3":
			print("\n OK, let's setup Master of Ceremony node")
			nodeType = 'moc'
		elif ans=="4":
			showMainMenu()
		elif ans=="5":
			print("\n Goodbye")
			exit()
		elif ans !="":
			print("\n What type of node? \n") 

def showUpdateNodeMenu():
	ans=True
	while ans:
		print ("""
		1. Update bootnode
		2. Update validator node
		3. Update moc node
		4. Go back to the main menu
		5.Exit/Quit
		""")
		ans=raw_input("...?") 
		if ans=="1": 
			print("\n 1")
			## show menu for node setup
		elif ans=="2":
			print("\n 2")
			## show menu for node update
		elif ans=="3":
			print("\n This option is not ready")
			showUpdateNodeMenu()
			## show menu for option 3
		elif ans=="4":
			showMainMenu()
		elif ans=="5":
			print("\n Goodbye")
			exit()
		elif ans !="":
			print("\n Not a valid choice. Try again \n")
			
def collectAWSInfo():
	print ("Enter AWS access_key:")
	access_key = input( "> " )
	
	print ("Enter AWS secret access_key:")
	access_key = input( "> " )

	print ("Enter MINING_KEYFILE - this should be a secret code provided to you by the Master of Ceremony")
	MINING_KEYFILE = input( "> " )

def collectBootnodeInfo():
	print ("Enter bootnode name. Should start with Bootnode. Example: 'Bootnode Atlanta' \n This would be visible to other members of the network")
	NODE_FULLNAME = input( "> " )

	print ("Enter your email. \n This would be visible to other members of the network")
	NODE_ADMIN_EMAIL = input( "> " )

	print ("Enter NETSTATS_SERVER - this should be a url provided to you by the Master of Ceremony")
	NETSTATS_SERVER = input( "> " )

	print ("Enter NETSTATS_SECRET - this should be a secret code provided to you by the Master of Ceremony")
	NETSTATS_SECRET = input( "> " )

def collectValidatorInfo():
	print ("Enter your FULL NAME. \n This would be visible to other members of the network")
	NODE_FULLNAME = input( "> " )

#def collectMocInfo():


	
showMainMenu()
