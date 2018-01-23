# poa-devops

poa-node-setup.py file can be used to setup different types of nodes for POA.Network (bootnode, valudator node, Master of Ceremony (MOC) node)

Currently all parameters should be added to a single "config.txt" file.

Things to add:

- Error checking, make sure SSH works with remote server before running ansible playboook => Important
- Menu for params, ability to specify node type, network type, etc. (Initial code is included and commented out)
- Improve match and replace functions with foreach loops key/value (Not critical)
- Remotely install Python on remote server via SSH and then run ansible playbook with paramiko (Python via SSS)
- Simplify config.txt format, so users don't have to worry about correct formmat - Done
- Add logging - Done


Update:

Tested on AWS. Currently it works only for validator node since boot node setup is slightly different


Process is simple:

    - User logs in to AWS and spins up new Ubuntu VM (this would be main / control VM). It could be vanilla VM without any modifications. (That could also be automated later)
    - From control VM (this would be powered on only when action on nodes is needs to be performed) user starts the script and gets a menu:

What would you like to do?

    1. Setup new node
    2. Update node
    3. Other action
    4. Exit

Then selects action, node type, network type, specifies other information that is needed. (in sub-menus)

    Done (everything is done automatically and minimizes user errors and support tickets). Also it assures that everything is in compliance and was setup properly.

Even creating and setting up VMs for nodes would be automated. After that, Control VM could be powered off. (Or it could monitor all nodes and perform other actions)

Things to consider:

Security. We would need audits for this code and for process, to make sure that all nodes are secure after running this script.

I believe for mass adoption that would be very beneficial. Users for example could easily spinup new bootnode. If there is a HF, they would power on control VM, start the script and update node.