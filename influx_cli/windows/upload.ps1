$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function askforconfigfile {
    .\influx.exe config list
}

function askforbuckets($bucket) {
    $json = .\influx.exe bucket list --json
    if (($json | ConvertFrom-Json).name -contains $bucket)
    {return $true}
}

function createnewbucket($bucket) {
    if(askforbuckets($bucket) -eq $true) {
        Write-Output 'Bucket already exists!'
    }
    else{
        .\influx.exe bucket create --name $bucket
        Write-Output $bucket "created"
    }
}

createnewbucket('Test2')


#if (askforbuckets('Claude') -eq $true) {
#    Write-Output 'hi'
#}
#else {
#    Write-Output 'bye'
#}

#askforconfigfile
#askforbuckets('Test')