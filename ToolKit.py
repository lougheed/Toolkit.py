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

#S3
def S3_File_Uploud(BucketName,FilePath):
    s3 = boto3.resource('s3')
    try:
        data = open(FilePath, 'rb')
        s3.Bucket(BucketName).put_object(Key='test.png', Body=data)
    except:
        print("Uanble to uploud file, make sure your bucket names is right and that AWS CLI config is setup") 
        

#EC2
def Whats_running():
    instances = ec2.instances.filter(#fix this
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print("ID: ", instance.id, "type:", instance.instance_type)
    Ask = input("Would you like to stop or terminate an instance? Y/N: ")
    if Ask == "y" or Ask == "Y" or Ask == "yes" or Ask == "Yes":
        What_instance = input("What instance would you to stop, enter the instance ID here: ")
        ids = 'i-062acb652d3a05d03'
        ec2.instances.filter(InstanceIds = id).stop()

    elif Ask == "n" or "N" or Ask == "no" or Ask == "NO" :
        pass
    else:
        print("Unknown inputer")

def create_instance():
    while true:
         AskUsr = input("To make a instance in AWS create or if you would to list out what EC2 create are running type list: ")

         if AskUsr == "create" or AskUsr == "CREATE":
             instance1 = "Amazon Linux AMI 2018.03.0 (HVM)"

             instance1_Image ='ami-031a03cb800ecb0d5'#sets the instance AMI to the the ARN of Amazon Linux AMI 2018.03.0 (HVM)
             #Calls the create_instances and sets up a new EC2 (bisc)
             instance_create = ec2.create_instances(
             ImageId= instance1_Image ,
             MinCount=1,
             MaxCount=1,
             InstanceType='t2.micro',
             )
             print("Set a t2.micro instance with the AMI", instance1)
         elif AskUsr == "list" or AskUsr == "LIST":#Some code I took form the doumention to list all the running ec2s, hey ifs its not broke.......
             instances = ec2.instances.filter(
                Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
             for instance in instances:
                 print(instance.id, instance.instance_type)


FilePath = 'test.png'
BucketName =  "pythontests"

S3_File_Uploud(BucketName,FilePath)
