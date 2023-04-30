$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function uploaddata($bucket, $csvfile){
    .\influx write --bucket $bucket --format=csv --file $csvfile
}
