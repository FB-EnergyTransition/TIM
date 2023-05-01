$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

# ask for config
. $PSScriptRoot\config.ps1 askforconfigfile

# ask for bucket
Write-Output "Please enter bucket"
$bucket = Read-Host
. $PSScriptRoot\bucketshandling.ps1 createnewbucket $bucket

# ask for csvfile and upload data
Write-Output "Please enter path of csvfile"
$csvfile = Read-Host
. $PSScriptRoot\upload.ps1 uploaddata $bucket $csvfile
