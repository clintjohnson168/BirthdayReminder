# BirthdayReminder
Reminder program that will send a text if someone's birthday is tomorrow.

This program uses a Birthday class that will hold a dictionary of birthdays.  Once the Birthday’s object has been initialized, birthdays can be added to the object using the .add(‘name’, month as int, day as int, year as int) command.  The .print() method will print out names and upcoming birthdates. The .checkBirthdays() will check to see if  a birthday is tomorrow, and if so will send an email/text using the information provide in the file.etxt file. This file needs to contain (on separate lines) the source email, the password to the source email account, and the destination email/phone address. 

The main function can be adjusted to send the message at different times of the day.
