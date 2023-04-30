import subprocess
import os

psexe = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
script_path = "{}\\callfunctions.ps1".format(os.path.dirname(os.path.abspath(__file__)))

commandline_options = [psexe, '-ExecutionPolicy', 'Unrestricted', script_path]  # ADD POWERSHELL EXE AND EXECUTION POLICY TO COMMAND VARIABLE

subprocess.run(commandline_options)  # CALL PROCESS

# subprocess.Popen([psexe, ".\"../callfunctions.ps1\";"])

# subprocess.call([psexe, ".\"../callfunctions.ps1\";"])

# # ask for bucket to upload data
# subprocess.call([psexe, ".\"../bucketshandling.ps1\";", "$createnewbucket(bucket)"])

# # print('Please enter bucket')
# # bucket = input()
#
# # https://www.appsloveworld.com/powershell/100/35/passing-variables-from-python-gui-to-powershell
# # subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",'-ExecutionPolicy','Unrestricted', '.\'./ScriptName\';','-printer',myPrinter])
#
# subprocess.call([psexe, ".\"../bucketshandling.ps1\";", "$createnewbucket", bucket])
# # subprocess.call([psexe, ".\"../bucketshandling.ps1\";", "$createnewbucket(bucket)"])
#
# # ask for csvfile
# print('Please enter csvfile')
# csvfile = input()
#
# subprocess.call([psexe, ".\"../upload.ps1\";", "$uploaddata(bucket, csvfile)"])
#
# # subprocess.call([psexe, ". \"../bucketshandling.ps1\";", "&askforbuckets"])
