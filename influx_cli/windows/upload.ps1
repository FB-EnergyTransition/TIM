$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function uploaddata($bucket, $csvfile){
    .\influx.exe write --bucket $bucket --format=csv --file $csvfile
}

uploaddata $bucket $csvfile