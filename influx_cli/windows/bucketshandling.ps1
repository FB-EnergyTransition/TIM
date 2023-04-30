$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function askforbuckets($bucket) {
    $json = .\influx.exe bucket list --json
    if (($json | ConvertFrom-Json).name -contains $bucket)
    {Write Output 'Bucket already exists!'
    return $true}
}

function deletebucket($bucket) {
    .\influx.exe bucket delete --name $bucket
}

function create($bucket) {
    .\influx.exe bucket create --name $bucket
#    Write-Output $bucket "created"
}

function createnewbucket($bucket) {
    if(askforbuckets($bucket) -eq $true) {
        Write-Output 'Bucket already exists! You want to delete the bucket and create it again (y/n)?'
        $choice = Read-Host
        if ($choice -eq 'y') {
            deletebucket($bucket)
            create($bucket)
        }
    }
    else{
        create($bucket)
    }
    return $bucket
}

#createnewbucket('Test2')
