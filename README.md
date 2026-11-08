# Mycs50Psubmissions

This repository includes all my submissions for cs50 Python weeks as well as a final_project. I have bundled the final project's main.py into a linux executable with all dependencies using pyinstaler.

## Contents

This section includes all the contents and their structures in a detailed manner

#### Python-submissions

It contains all the submissions for each week of the course. In the folder, each week has a separate folder which has the submissions. *some* weeks might have a test or practice directory which includes the stuff i practiced. You can safely ignore it.

#### final_project

It contains the final project of mine. Which includes
	- main.py
	- requirements.txt
	- README.md (for the final project)
	- test_main.py (Well this is a formality, I left it simple cause if some functions worked successfully, remaining would automatically do the same)

#### main
It is an executable which has been made using pyinstaller

##### How to use it
SInce I have made it on Linux Mint 22.3 . It might work only on similar environments.

###### If you _OS_ is comaptible

```
cd Mycs50Psubmissions
./main
```
 
###### If not (build from source)

```
cd Mycs50Psubmissions
cd final_project
python -m venv .venv
source .venv/bin/activate
pip install pyinstaller
pip install -r requirements.txt
pyinstaller --onefile main.py
```
Now, if you have done correctly. The executable will live in dist
```
cd dist
./main
```

##### Features
It has options like 
	- Search for username availability
	- Get the Github Id
and 6 more. Take a look yourself.

##### How it works

 If you selected an option which used regex. It used a regex pattern which i found online. I am not sure if its right. As regex feels confusing for me.

 If you selected other options it uses github's [API Endpoint for users](https://api.github.com/users/username)


 
## AI usage
Cs50's own duck debugger has been used while taking the lessons and doing the problem sets. Ai has not been used in making the final project or the executable.

## Quick Links

 - [Cs50 Python](https://cs50.harvard.edu/python)
 - [My github profile](https://github.com/CuriousDudeDev)
 - [My cs50 Project submission video](https://youtu.be/L2-yDOtd2n4)
