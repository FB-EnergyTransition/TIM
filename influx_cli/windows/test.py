import subprocess

psexe = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"

subprocess.call([psexe, ". \"../upload.ps1\";", "&askforbuckets"])
