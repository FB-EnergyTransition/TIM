import subprocess
import os

psexe = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
script_path = "{}\\callfunctions.ps1".format(os.path.dirname(os.path.abspath(__file__)))

commandline_options = [psexe, '-ExecutionPolicy', 'Unrestricted', script_path]

subprocess.run(commandline_options)