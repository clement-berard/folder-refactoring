# 
# author CLEMENT BERARD
# 22/02/2017

# files filters
fileFilter = ['.DS_Store']
allowedExtension = ['avi', 'mkv', 'mp4', 'mp3', 'srt', 'sub', 'mov', 'txt']
resultFolderName = 'result'
simulation = 1
removeFolder = 0

# imports
import os, sys, shutil, argparse

parser = argparse.ArgumentParser(description='Move all files in folder recursively. Allowed extensions : ' + str(allowedExtension))

parser.add_argument('--ext', 
                    help='Add some extension allowed e.g. --ext=txt,svg,jpg')
parser.add_argument('--no-files',
                    help='Add name of files non allowed to move e.g. --no-files=example.txt,foo.bar')
parser.add_argument('--dest',
                    help='Name of result folder (Default : '+ resultFolderName +')')
parser.add_argument('--simu',
                    help='No real move of files (Default : 1)')
parser.add_argument('--remove-folders',
                    help='Remove all folder (Default : 0)')

# get all arguments
args = parser.parse_args()
# simulation
if (args.simu):
    simulation = int(args.simu)
# Remove folders
if (args.remove_folders):
    removeFolder = int(args.remove_folders)
# for extensions of files
if (args.ext):
    more_ext = args.ext.split(',')
    allowedExtension = allowedExtension + more_ext


if (args.no_files):
    more_exclude_files = args.no_files.split(',')
    fileFilter = fileFilter + more_exclude_files


# args
totalArguments = len(sys.argv)
# add script name to the forbidden file to move
scriptName = sys.argv[0]
fileFilter.append(scriptName)



# get current folder
current = os.getcwd()
print "*************************************"
if simulation:
    print "!! SIMULATION MODE !! To change, add --simu=0"
print "## Current folder : " + current
print "*************************************"

# increment for total of files
i = 0

# creation du dossier de sortie
resultFolder = current + "/" + resultFolderName
if not os.path.exists(resultFolder) and not simulation:
    os.makedirs(resultFolder)

# loop on root folder (current folder)
for root, subdirs, files in os.walk(current):
    # no files in root dir
    if root != resultFolder:
        for filename in files:
            if filename not in fileFilter:
                # get extension
                extension = os.path.splitext(filename)[1][1:]
                # get file path
                file_path = os.path.join(root, filename)
                # if file has an allowed extension
                if extension in allowedExtension:
                    i = i + 1
                    print "-------------------------------"
                    print "--> " + filename 
                    if not simulation:
                        shutil.move(file_path, resultFolder)


# delete folders after copy
print "*************************************"

print "List of remove folder : "

for root, subdirs, files in os.walk(current):
    if root != resultFolder and root != current:
        print root
        if os.path.exists(root):
            if not simulation and removeFolder:
                shutil.rmtree(root)
                
                
                

# print final
print "=================================="
print "Total : " + str(i)
print "=================================="