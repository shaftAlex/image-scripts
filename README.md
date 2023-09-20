
# Image Scripts
This is a collection of scripts, mostly complex bulk image operations, that I have written to speed up my workflow. I plan to add more over time as I need them. Are you familiar with GitHub and Python? Skip to [the dependencies](#dependencies).

## Quick Start Guide
It looks lengthy but I promise its only because I hate when quick start guides aren't tailored for people with zero development experience. Also, this guide is for Windows because I've never used other operating systems. 

### 1: Download + Extract
- If you are not familiar with GitHub, don't worry! To download the most recent version click [this link](https://github.com/shaftAlex/image-scripts/archive/refs/heads/main.zip).
- Unzip the file and put it wherever you want! OK I lied, anywhere except for folders that require administrator to access (i.e. operating system folders).

### 2: Install Python
You will need [Python](https://www.python.org/downloads/) installed to run these scripts.
- You can check if Python is installed and up-to-date by opening a Command Prompt and running `python --version`. These scripts were written and tested with Python 3.11.5 but they should run with pretty much any version that isn't archaic.
- If the Command Window gave you an error you need to install Python. Head over to [the Python website](https://www.python.org/downloads/) and click the Download button. It should autodetect your hardware and operating system. 
- Run the installer
- On the first page, **please select "Add Python 3.8 to PATH"** cause it will make your life much easier. Then just click Install Now. You do not need to customize the installation.
- At some point it will ask if you want to remove the MAX_PATH limitation. Please agree to remove the limitation. 
- Whenever it is done, just close the installer, open up a Command Prompt and run `python --version` again to check that it is installed correctly.

### 3: Setup Python Environment
These scripts have dependencies that you will need to install for them to work. Here's how you do it:
- Navigate to the folder that contains the scripts and type `cmd` into the address bar at the top of the file explorer. Then hit enter, this opens a Command Prompt that will run in that folder. 
- Run the commands listed in [the dependencies](#dependencies) section one by one. 

### 4: Using the Scripts
- Anytime you want to use the scripts, go to the folder that contains them and type `cmd` into the address bar like in step 3a. 
- To run a script, type `python` or `py` followed by the name of the script. It must include the `.py`. For example, `python deleteBlanks.py`.
- From here, the script will ask you for any information it needs, usually just the folder to look through, but sometimes it asks for more. 

That's all there is to it! Just remember, *there is no undo!!!*

## Dependencies
```pip install pillow```

Yeah that's the only one for now :3