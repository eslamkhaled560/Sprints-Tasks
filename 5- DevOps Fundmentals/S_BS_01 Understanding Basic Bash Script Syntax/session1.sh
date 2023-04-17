#!/bin/bash
echo "This script will print variables, and execute Linux commands"
# (nin>bin) and (Echo>echo) 


# Functions for environment deails
function current_dir {
	echo "Current Working Directory is: $(pwd)"
    	echo "Exit Code: $?"
	echo ---------------------------------------------------------------------------------------
}

function current_user {
	echo "Currenr User who's logged in is: $(whoami) "
	echo "Exit Code: $?"
	echo ---------------------------------------------------------------------------------------
}

function files_in_home {
	echo "All files in Home Directory in details:"
	ls -la ~
	echo "Exit Code: $?"
}

# Call each function
echo ---------------------------------------------------------------------------------------
echo "Here is some details about my environment:"
echo
current_dir
current_user
files_in_home
echo ---------------------------------------------------------------------------------------
