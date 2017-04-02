import time
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#uses the file.etxt file that holds source email, password and
#  destination email information

class Birthdays:
    #constructor
    def __init__(self):
        self.birthdays = {}
        self.now = datetime.now()
        self.tomorrowsDate = "%s-%s" %(self.now.month, self.now.day + 1)
        self.updateDate()
    
    #add a birthday to the dictionary
    #   monthDay(m-dd) as string
    def add(self, name, month, day, year):
        self.birthdays[name] = [month, day, year]

    #print out the dictionary
    def print(self):    
        if self.birthdays.items():
            self.updateDate()            
            for name, pair in self.birthdays.items():
                birthday = "%s-%s" %(pair[0], pair[1])
                if self.now.month > pair[0]:
                    print("%s's birthday is on %s-%s-%s" %(name, pair[0], pair[1], self.now.year + 1))
                elif self.now.month >= pair[0] and self.now.day > pair[1]:
                    print("%s's birthday is on %s-%s-%s" %(name, pair[0], pair[1], self.now.year + 1))
                else:
                    print("%s's birthday is on %s-%s-%s" %(name, pair[0], pair[1], self.now.year))
                
            print("")
        else:
            print("No birthdays have been entered.\n")
            
    #Gets tomorrow's date (mm-dd)
    def updateDate(self):
        self.now = datetime.now()
        tomorrow = self.now + timedelta(days=1)
        self.tomorrowsDate = "%s-%s" %(tomorrow.month, tomorrow.day)
        #print(self.tomorrowsDate)

    #update date and check birthdays
    def checkBirthdays(self):
        self.updateDate()
        for item, pair in self.birthdays.items():
            #print("Checked %s's birthday" %(item))
            birthday = "%s-%s" %(pair[0], pair[1])
            if(birthday == self.tomorrowsDate):
                subject = "It is %s's birthday tomorrow!" %(item)
                age = self.now.year - int(pair[2])
                message = "%s will be %s year(s) old. " %(item, age)
                print("It is %s's birthday tomorrow!" %(item))
                print("%s will be %s year(s) old. " %(item, age))
                self.sendMessage(subject, message)
            else:
                print ("%s's birthday is not tomorrow. " %(item))
        print("")
        

    #crate and send email text
    def sendMessage(self, subject, message):
        source, password, destination = self.getEmail()

        try:
            #create smtp object
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            #login to server
            server.login(source, password)

            #create message content
            content = MIMEMultipart()
            content["Subject"] = subject     #"%s's Birthday Reminder" %(name)
            content["From"] = source
            content["To"] = destination
            content.attach(MIMEText(message))
            content.attach(MIMEText("\nMessage was sent at %s" %(datetime.now())))

            #send message
            server.sendmail(source, destination, content.as_string())
            #print(content.as_string())
            
            #close server
            server.close()
            print("Message sent")
        except():
            print("Error sending message")
            

    #get email address and password from file
    def getEmail(self):
        try:
            file = open("file.etxt", 'r')
            email = file.readline()
            password = file.readline()
            destination = file.readline()
            return email, password, destination
        except ():
            print("Error reading file")
        finally:
            file.close()

def main():
    birthdays = Birthdays()
    #add birthdays from birthdays.etxt file
    with open('birthdays.etxt', 'rb') as file:
        for line in file:
            words = line.split()
            name = words[0].decode("utf-8")
            month = int(words[1])
            day = int(words[2])
            year = int(words[3])
            print(name)
            birthdays.add(name, month, day, year)

    #verify birthdays have been added
    birthdays.print()
    
    #check to see if it is 7 every 60 seconds
    while(True):
        now = datetime.now()
        hourMinutes = "%s:%s" %(now.hour, now.minute)
        print("It is currently %s (h:m)" %(hourMinutes))
        #check for birthdays at 7pm 
        if(hourMinutes == "19:0"):
            birthdays.checkBirthdays()
        time.sleep(60)

main()
