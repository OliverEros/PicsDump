### PicsDump
<img src =https://i.imgur.com/wZBrupw.png align='center'>
Automising unused image deletion for HTML emails/e-shots.

## Intro:
Used to delete images from the image folder based on whether the filename was mentioned in the HTML file. Created to speed up having to go through old pictures manually.

## How it works?
The structure of HTML e-mails comprises of two things: the index.html file and the image folder. The script uses two parsers, one for the file and one for the folder. Using regex, we find anything ending with .gif or .jpg. Then the folder is scanned as well. Mismatches are deleted. <b>As of 03/04/21 Windows is supported! </b>


## Installation
A setup.py file has been added. To install, use 'pip3 install <directory>" 

## How to use?
The program will prompt you to enter the path of your HTML e-email (parent folder which has the image folder and the index.html file). 

## Safe mode
If argument 's' is provided, the program will not delete the images but rather prints their name. (In case you would rather remove them manually)

## Limitations
1. The folder for the images must be called 'images' and the HTML file must be called 'index.html'

## To Come
Enabling custom image folder and HTML file name

