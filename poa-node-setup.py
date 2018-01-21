#!/usr/bin/env python

### Authtor: Marat Pekker
### Date: Jan/20/2018
### Description: This script is for setting up  POA.network nodes. (bootnode, validator node, Master of Ceremony (MOC) node)
### Things to add: Menu for params, ability to specify node type, network type, etc. Improve match and replace functions with foreach loops key/value
### Error checking, make sure SSH works with remote server before running ansible playboook

import os
import sys
import fileinput

def getVarFromFile(filename):
	import imp
	f = open(filename)
	global data
	data = imp.load_source('data', '', f)
	f.close()

def replace()
	for i, line in enumerate(fileinput.input('all', inplace=1)):
	sys.stdout.write(line.replace(old, new))
	
# Get all params from config.txt (later we will also add a menu)
getVarFromFile('config.txt')

## Install ansible
os.system ('sudo pip install ansible')

## Install packages
os.system ('sudo pip install boto')
os.system ('sudo pip install boto3')

## Make sure you have latest AWS CLI
os.system ('pip install awscli --upgrade --user')

## Download and configure playbook
os.system ('cd ..')
os.system ('git clone https://github.com/poanetwork/deployment-playbooks.git')
os.system ('cd deployment-playbooks')
# for core mainnet
# os.system('git checkout core')
# OR for sokol testnet
os.system ('git checkout sokol')
# check that you ended up on a correct branch (look where the `*` is)
os.system ('git branch')

## Prepare SSH keys (asummes you already have SSH keys for remote server)
os.system ('cat ~/.ssh/id_rsa.pub > files/admins.pub')
os.system ('cp files/admins.pub files/ssh_validator.pub')

os.system ('cat group_vars/all.network group_vars/validator.example > group_vars/all')

## Start replacing params (This cloud be improved with foreach loops and key/value match and replace)

##------------------------------------------------------------------
old = 'access_key: "INSERT KEY HERE"'
new = 'access_key: "' + data.access_key + '"'
replace()
##------------------------------------------------------------------
old = 'secret_key: "INSERT SECRET HERE"'
new = 'secret_key: "' + data.secret_key + '"'
replace()
##------------------------------------------------------------------
old = 'awskeypair_name: "keypairname"'
new = 'awskeypair_name: "' + data.awskeypair_name + '"'
replace()
##------------------------------------------------------------------
old = 'NODE_FULLNAME: "INSERT NODENAME"'
new = 'NODE_FULLNAME: "' + data.NODE_FULLNAME + '"'
replace()
##------------------------------------------------------------------
old = 'NODE_ADMIN_EMAIL: "INSERT@EMAIL"'
new = 'NODE_ADMIN_EMAIL: "' + data.NODE_ADMIN_EMAIL + '"'
replace()
##------------------------------------------------------------------
old = 'NETSTATS_SERVER: "INSERT FULL URL"'
new = 'NETSTATS_SERVER: "' + data.NETSTATS_SERVER + '"'
replace()
##------------------------------------------------------------------
old = 'NETSTATS_SECRET: "INSERT SECRET"'
new = 'NETSTATS_SECRET: "' + data.NETSTATS_SECRET + '"'
replace()
##------------------------------------------------------------------


##------------------------------------------------------------------
old = 'MINING_KEYFILE: \'INSERT HERE\''
new = 'MINING_KEYFILE: ' + data.MINING_KEYFILE
replace()
##------------------------------------------------------------------
old = 'MINING_ADDRESS: "INSERT HERE"'
new = 'MINING_ADDRESS: "' + data.MINING_ADDRESS + '"'
replace()
##------------------------------------------------------------------
old = 'MINING_KEYPASS: "INSERT HERE"'
new = 'MINING_KEYPASS: "' + data.MINING_KEYPASS + '"'
replace()
##------------------------------------------------------------------

##------------------------------------------------------------------
old = 'allow_validator_ssh: true'
new = 'allow_validator_ssh: ' + data.allow_validator_ssh
replace()
##------------------------------------------------------------------
old = 'allow_validator_p2p: true'
new = 'allow_validator_p2p: ' + data.allow_validator_p2p
replace()
##------------------------------------------------------------------
old = 'associate_validator_elastic_ip: false'
new = 'associate_validator_elastic_ip: ' + data.associate_validator_elastic_ip
replace()
##------------------------------------------------------------------

## Create hosts file and add server IP
## We will need to add params here to specify correct node type
cmd = "echo [validator] > hosts"
os.system(cmd)
cmd = "echo " + SERVER_IP + " >> hosts"
os.system(cmd)

# run this script to configure the instance (might want to use paramiko - ssh via python)
os.system ('ansible-playbook -i hosts site.yml')

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