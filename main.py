# I'm tired of sending a mail to myself, for every LAB OUTPUT AND CODE. It is ridiculous. I hate it.
# EOR


# The following program relies on Yagmail, which greatly simplifies the process compared to using a SMTP lib.
# Downside being yagmail is INCOMPATIBLE for 3.11.x as of making this program on 26/09/03 (26th September 2023)

import yagmail
from customScreenShot import Application
from tkinter import *
import os

def getTopicName():
    
    print("Enter a topic name : ")
    topic = input("")

    return topic

    
    


def runScreenShotApp(directoryName : str):
    directoryExisting = os.path.exists("./" + directoryName)

    if not directoryExisting:
        os.makedirs("./" +directoryName)


    root = Tk()
    app = Application(root, directoryName)
    root.mainloop()




def sendMail(topic : str):
    reciever = input("Enter Your Email Address : ")

    if reciever == "":
        senderMail(topic)
        return

    senderMail = "getintouchwithvic2@gmail.com"
    app_password = "psrp obdl stym opck"
    yag = yagmail.SMTP(senderMail, app_password)

    

    
    body = f"""
        Mail regarding {topic} 
        
        This mail was sent by a helper bot, please ignore if this wasnt requested by you
    
    """

    screenshots = [open(topic + "/" + file, 'rb') for file in os.listdir(topic) if file.endswith('.png')]


    yag.send(to=reciever, subject=topic, contents=body, attachments=screenshots)


#main here

def main():
    topic = input("Provide a name for the topic : ")
    if(topic == ""):
        return
    runScreenShotApp(topic)
    sendMail(topic)
    print("Sent Mail.")


if __name__ == "__main__":
    main()



