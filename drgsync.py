#DRG save syncer
#Author: James Bramnick
import os
import shutil

#Simply change the folders to your paths to steam saves and xbox saves follow this post to find out where your folders are: https://www.reddit.com/r/DeepRockGalactic/comments/e7hptr/how_to_transfer_your_steam_save_to_windows_10_and/
xboxFolder=r"C:\Path\to\folder"
steamFolder=r"C:\Path\to\folder"

def sync():
    steamFile=""
    xboxFile=""
    xboxFileName=""
    steamFileName=""
    xtime = None
    stime = None
    xbackNum = 0
    sbackNum = 0
    for file in os.listdir(xboxFolder):
            
        if "." not in file:
                xboxFile=os.path.join(xboxFolder,file)
                xtime = os.path.getmtime(xboxFile)
                xboxFileName = file
        if file.endswith(".bak"):
                temp = int(file.split("__")[1])
                if temp >= xbackNum:
                                xbackNum = temp+1
    for file in os.listdir(steamFolder):
        if file.endswith('_Player.sav'):
                steamFile=os.path.join(steamFolder,file)
                stime = os.path.getmtime(steamFile)
                steamFileName = file
        if file.endswith(".bak"):
                temp = int(file.split("__")[1])
                if temp >= sbackNum:
                                sbackNum = temp+1
    if stime > xtime:
            shutil.copy(xboxFile,os.path.join(xboxFolder,xboxFileName+"__"+str(xbackNum)+"__.bak"))
            shutil.copy(steamFile,xboxFile)
            print ("Steam file copied to xbox")
    elif xtime > stime:
            shutil.copy(steamFile,os.path.join(steamFolder,steamFileName+"__"+str(sbackNum)+"__.bak"))
            shutil.copy(xboxFile,steamFile)
            print ("Xbox file copied to steam")
    else:
        print ("Something is wonky or your files have the exact same time maybe play some DRG. Rock and Stone brother")
def main():
    sync()
    input("Press any key to close application")
if __name__ == "__main__":
        main()