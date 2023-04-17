# Session 1 - Bash Scripting Basics

**Presented to:**    
_Omar Mohsen_    

**Presented by:**   
_Islam Khaled_    

17 April 2023

-----------------------------------------
### The Script:

The original script is provided [session1.sh](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/5-%20DevOps%20Fundmentals/S_BS_01%20Understanding%20Basic%20Bash%20Script%20Syntax/session1.sh) , 
and here is the code inside the script:
```
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
```     

-------------------------
### The Output:      
![image](https://user-images.githubusercontent.com/54172897/232524544-9ce2d3ae-3d25-472b-8cf2-ecfbace2648e.png)

------------------
