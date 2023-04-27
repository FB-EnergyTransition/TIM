function askforconfigfile {
    cd 'C:\Program Files\InfluxData\influx\'
    .\influx.exe config list
}

function askforbuckets {
    cd 'C:\Program Files\InfluxData\influx\'
    .\influx.exe bucket list
}

askforconfigfile
askforbuckets