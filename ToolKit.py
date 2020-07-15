from gtts import gTTS
import os,shutil,boto3
from time import sleep
from playsound import playsound
from sys import*

def TextToSpeech(UsrTxt):#method to trun text to a MP3 flie
    language = "en"#set gTTS vars
    speech = gTTS(text = str(UsrTxt), lang = language, slow = False)#set the lan and convert var into a string
    speech.save("voice.mp3")#Useing gTTS save the the string as a MP3 file
    playsound("voice.mp3")#useing playsound to run the MP3 file
    sleep(2)
    #ask the suer if they would like to keep the file
    AskUsr = input("Would you like to remove the mp3 file? ")#Ask user if they would like to keep the MP3 file
    if AskUsr == "yes" or "y":
        os.remove("voice.mp3")
        print("voice.mp3 removed")
    else:
        print("OK the file can be found at ",os.getcwd())
        exit()


def Move_File(FileName):
    PWD = os.getcwd()#Get the current working dir
    if platform == "linux" or platform == "linux2":#If linux do this
        print("linux")
    elif platform == "darwin":#If MAC
        print("MAC")
    elif platform == "win32":#If windows
        FileName = PWD + "\\" + FileName#Puts PWD together with the file
        WhoAmI = os.getlogin()# find the logned user will user this info in the next line
        DownloudFolder = r"C:\Users\\" + WhoAmI + "\Downloads"#sets the downloud folder for the file
        shutil.move(FileName, DownloudFolder )#Useing shutil to move the file
        print("File is at", DownloudFolder )#Tell the user where to find the file

"""
AWS tools here
"""

def S3_File_Uploud(BucketName,FilePath):
    s3 = boto3.resource('s3')
    try:
        data = open(FilePath, 'rb')
        s3.Bucket(BucketName).put_object(Key='test.png', Body=data)
    except:
        print("Uanble to uploud file, make sure your bucket names is right and that AWS CLI config is setup") 

FilePath = 'test.png'
BucketName =  "pythontests"

S3_File_Uploud(BucketName,FilePath)
