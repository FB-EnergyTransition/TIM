$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function askforconfigfile {
    .\influx.exe config list
}

function askforbuckets {
    $json = .\influx.exe bucket list --json
    ($json | ConvertFrom-Json).name
}

#askforconfigfile
#askforbuckets