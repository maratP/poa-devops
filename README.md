# poa-devops

poa-node-setup.py file can be used to setup different types of nodes for POA.Network (bootnode, valudator node, Master of Ceremony (MOC) node)

Currently all parameters should be added to a single "config.txt" file.

Things to add:

- Menu for params, ability to specify node type, network type, etc. (Initial code is included and commented out)
- Improve match and replace functions with foreach loops key/value (Not critical)
- Error checking, make sure SSH works with remote server before running ansible playboook => Important
- Remotly install Python on remote server via SSH and then run ansible playbook with paramiko (Python via SSS)
- Simplify config.txt format, so users don't have to worry about correct formmat and " v.s. \"
