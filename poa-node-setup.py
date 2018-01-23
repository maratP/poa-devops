#!/usr/bin/env python

import os
import sys
import fileinput

#import poaMenu

def getVarFromFile(fileName):
	import imp
	f = open(fileName)
	global data
	data = imp.load_source('data', '', f)
	f.close()

def replace(oldStr,newStr,fileName):
	for i, line in enumerate(fileinput.input(fileName, inplace=1)):
		sys.stdout.write(line.replace(oldStr, newStr))
			

# Get all params from config.txt (later we will also add a menu)
getVarFromFile('config.txt')


#sudo apt-get update && sudo apt-get -y upgrade
#sudo apt-get install python-pip
#sudo apt install git

## Install ansible
print ("Installing Ansible\n==========\n")
os.system ('sudo pip install ansible')

## Install packages
print ("Installing boto and boto3\n==========\n")
os.system ('sudo pip install boto')
os.system ('sudo pip install boto3')

## Make sure you have latest AWS CLI
print ("Making sure you have latest AWS CLI\n==========\n")
os.system ('pip install awscli --upgrade --user')

## Download and configure playbook
print ("Downloading Ansible playbook\n==========\n")
os.chdir ('/home/ubuntu')
os.system ('git clone https://github.com/poanetwork/deployment-playbooks.git')
os.chdir ('deployment-playbooks')
# for core mainnet
# os.system('git checkout core')
# OR for sokol testnet
#os.system ('git checkout sokol')

print ("Selecting correct branch based on specified network type: [" + networkType + "]\n==========\n")
cmd = "git checkout " + networkType
os.system (cmd)

# check that you ended up on a correct branch (look where the `*` is)
os.system ('git branch')

## Prepare SSH keys (asummes you already have SSH keys for remote server)
print ("Coping SSH keys\n==========\n")
os.system ('cat ~/.ssh/id_rsa.pub > files/admins.pub')
#os.system ('cp files/admins.pub files/ssh_validator.pub')
cmd = "cp files/admins.pub files/ssh_" +nodeType+ ".pub"
#os.system ('cmd')

print ("Configuring based on node type: [" +nodeType+ "]\n==========\n")
#os.system ('cat group_vars/all.network group_vars/validator.example > group_vars/all')
cmd = 'cat group_vars/all.network group_vars/'+nodeType+'.example > group_vars/all'
os.system (cmd)


## Start replacing params (This cloud be improved with foreach loops and key/value match and replace)
#scriptpath = os.path.dirname(__file__)
#scriptpath = "/home/ubuntu"
#fileName = os.path.join(scriptpath, 'deployment-playbooks/group_vars/all')


os.chdir ('/home/ubuntu/deployment-playbooks/group_vars')

print ("Updating files with your information...\n==========\n")

#testFile=open(filename)
fileName = "all"
##------------------------------------------------------------------
oldStr = 'access_key: "INSERT KEY HERE"'
newStr = 'access_key: "' + data.access_key + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'secret_key: "INSERT SECRET HERE"'
newStr = 'secret_key: "' + data.secret_key + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'awskeypair_name: "keypairname"'
newStr = 'awskeypair_name: "' + data.awskeypair_name + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'NODE_FULLNAME: "INSERT NODENAME"'
newStr = 'NODE_FULLNAME: "' + data.NODE_FULLNAME + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'NODE_ADMIN_EMAIL: "INSERT@EMAIL"'
newStr = 'NODE_ADMIN_EMAIL: "' + data.NODE_ADMIN_EMAIL + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'NETSTATS_SERVER: "INSERT FULL URL"'
newStr = 'NETSTATS_SERVER: "' + data.NETSTATS_SERVER + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'NETSTATS_SECRET: "INSERT SECRET"'
newStr = 'NETSTATS_SECRET: "' + data.NETSTATS_SECRET + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------


##------------------------------------------------------------------
oldStr = 'MINING_KEYFILE: \'INSERT HERE\''
newStr = 'MINING_KEYFILE: \'' + data.MINING_KEYFILE + '\''
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'MINING_ADDRESS: "INSERT HERE"'
newStr = 'MINING_ADDRESS: "' + data.MINING_ADDRESS + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'MINING_KEYPASS: "INSERT HERE"'
newStr = 'MINING_KEYPASS: "' + data.MINING_KEYPASS + '"'
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------


oldStr = 'vpc_subnet_id = "subnet-ID-number"'
newStr = 'vpc_subnet_id: ' + data.vpc_subnet_id
replace(oldStr,newStr,fileName)


##------------------------------------------------------------------
oldStr = 'allow_validator_ssh: true'
newStr = 'allow_validator_ssh: ' + data.allow_validator_ssh
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'allow_validator_p2p: true'
newStr = 'allow_validator_p2p: ' + data.allow_validator_p2p
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------
oldStr = 'associate_validator_elastic_ip: false'
newStr = 'associate_validator_elastic_ip: ' + data.associate_validator_elastic_ip
replace(oldStr,newStr,fileName)
##------------------------------------------------------------------

## Create hosts file and add server IP
## We will need to add params here to specify correct node type
print ("Creating HOSTS file\n==========\n")
os.chdir ('/home/ubuntu/deployment-playbooks')
#cmd = "echo [validator] > hosts"
cmd = "echo ["+nodeType+"] > hosts"
os.system(cmd)
cmd = "echo " + data.SERVER_IP + " >> hosts"
os.system(cmd)

# run this script to configure the instance (might want to use paramiko - ssh via python)
print ("Running Ansible playbook and deploying\n==========\n")
os.system ('ansible-playbook -i hosts site.yml')


print ("Done\n==========\n")
## End of script

#### Additional items for improvements:

## Menu:
###-------------------------------------
#print ("Enter AWS access_key:")
#access_key = input( "> " )

#print ("Enter your FULL NAME. \n This would be visible to other members of the network")
#NODE_FULLNAME = input( "> " )

#print ("Enter your email. \n This would be visible to other members of the network")
#NODE_ADMIN_EMAIL = input( "> " )

#print ("Enter NETSTATS_SERVER - this should be a url provided to you by the Master of Ceremony")
#NETSTATS_SERVER = input( "> " )

#print ("Enter NETSTATS_SECRET - this should be a secret code provided to you by the Master of Ceremony")
#NETSTATS_SECRET = input( "> " )

#print ("Enter MINING_KEYFILE - this should be a secret code provided to you by the Master of Ceremony")
#MINING_KEYFILE = input( "> " )


## Also we could add a function to generate SSH keys and upload to remote server
# ssh-keygen -t rsa -b 4096 -C "your_email@example.com"