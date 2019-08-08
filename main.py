#!/usr/bin/env python

import os

def runApp(name):
    cmd = "gtk-launch "+name
    os.system(cmd)

import re
def findDesktopFiles(path):
    if path[-1] == "/": path = path[:-1]
    files = []
    directoryTree = os.walk(path)
    for dirName, subdirList, fileList in directoryTree:
        for fname in fileList:
            files.append(path+"/"+fname)
        break
    return files

def parseDesktopFile(text):
    regex = lambda x: x+"=(.*[^\n])\n"
    toRetrieve = ["Name", "Comment", "Icon", "Exec"]
    data = []
    for value in toRetrieve:
        matchObj = re.search(regex(value), text)
        data.append(matchObj.group(1) if matchObj != None else None)
    return tuple(data)

def appListGenerate():
    files = findDesktopFiles("/usr/share/applications") + findDesktopFiles("./local/share/applications") 
    data = []
    for name in files: 
        with open(name, "r") as desktopFile:      
            data.append(parseDesktopFile(desktopFile.read()))
    return data
#button.props.image = gtk.image_new_from_icon_name('emblem-favorite', gtk.ICON_SIZE_BUTTON)

def main(args):
    pass
    #runApp("virtualbox.desktop")
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
