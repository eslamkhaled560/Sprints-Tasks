#!/bin/bash
echo "This script will print variables, and execute Linux commands"
# (nin>bin) and (Echo>echo)


# Functions for environment deails
function current_dir {
	echo "Current Directory:"
    pwd
    echo "Exit Code: $?"
	echo
}

function current_user {
	echo "Current User:"
    whoami
    echo "Exit Code: $?"
	echo
}

function files_in_home {
	echo "All Files in Home Directory:"
    ls -la ~
    echo "Exit Code: $?"
}

# Call each function
echo
current_dir
current_user
files_in_home