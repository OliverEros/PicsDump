# PicsDump
Automatizing unused image deletion for HTML emails/e-shots.

## Intro:
At work, my main responsibily is to create HTML e-mails (also called e-shots) for different clients. To speed up the crocess, sometimes we use existing templates from the past that have the same layout but use images that are not needed anymore. The completed work then gets uploaded to a server, therefore it is important that we do not have reduntant data taking up space such as the previously mentioned images. Unfortunately, sometimes I forget to delete them...so why not use automation instead? 

## How it works?
The structure of HTML e-mails comprises of two things: the index.html file and the image folder. The script uses two parsers, one for the file and one for the folder. First, the file is essentially scraped and then using regex, anything ending with .gif or .jpg is saved into a set. Then the folder is scanned as well. At last, the two sets are compared and anything that is not both gets deleted.

## How to use?
The program will prompt you to enter the path of your HTML e-email (parent folder which has the image folder and the index.html file). 

## Safe mode
If argument 's' is provided, the program will not delete the images but rather prints their name. (In case you would rather remove them manually)

## Limitations
1. The folder for the images must be called 'images' and the HTML file must be called 'index.html'

