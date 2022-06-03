# JackPass Manager

JackPass Manager is a python application that uses the PyQt5 library and QtDesigner in its development. This application applies an encryption method to passwords in the sqlite3 database using three algorithms namely md5, AES128, and base64.

![App](https://user-images.githubusercontent.com/82703688/171824444-4d644bf4-3e55-4047-a7fb-a827012c26e2.png)

Content : 

Login Menu : Default Credential is username 'admin' and password 'admin' 

Dashboard Page: 
- Create data menu : Input field for website,email, and password
- See credential menu : 
	- A table view for showing user data.
	- Show password and delete data button only trigerred when you click the id column.
	- Delete all entries.
- Logout : Exit Application
