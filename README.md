# Project-Mail
A python software that sends email throughout terminal so that you don't have to login to your Gmail everytime. (Note that this is only for Gmail, and any other domain.)

#### How to set-up?: Cd to the Project-Mail folder, and open creds.json as a text file.
#### You should see this:
```
{ 
	"login": {
		"email": "your email here",
		"password": "your password here"
	}
}
```
#### Put your email and password where it tells you to.
#### Your creds.json file should look like something like this: 
```
{ 
	"login": {
		"email": "example@gmail.com",
		"password": "password123"
	}
}
```
#### Please note that you put your own information. That is just an example.

#### After that is complete, save the file and close it.

#### How to use?: Cd to the Project-Mail (if not there), and run this:
```
python3 main.py targetemail@domain.com 
```
#### Of course, change the "targetemail@domain.com" to the target email you are sending to. I.E HyperNovae@yahoo.com.

#### After running, you should see this:
```
Input what to send for specified email(use quotation marks): 
```
#### Start writing your message, and press enter.
#### Make sure your message has quotation marks, else it would send an empty email.
#### An example:
```
Input what to send for specified email(use quotation marks: "Hello, world!"
```
#### IF you did everything right, you should see "Job has successfully finished."

