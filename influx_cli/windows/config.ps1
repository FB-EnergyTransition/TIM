$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function askforconfigfile {
    .\influx.exe config list --json
}
