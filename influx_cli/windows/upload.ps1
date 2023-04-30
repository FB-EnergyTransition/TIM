$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function askforconfigfile {
    .\influx.exe config list
}

function askforbuckets {
#    cd 'C:\Program Files\InfluxData\influx\'
    .\influx.exe bucket list
}

askforconfigfile
askforbuckets