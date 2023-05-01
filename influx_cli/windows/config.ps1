$dir = Join-Path -Path $PSScriptRoot -ChildPath "\influx"
cd $dir

function askforconfigfile
{
    if (.\influx.exe config TIM)
    {
        Write-Output 'Config TIM exists'
    }
    else
    {
        .\influx.exe config create --config-name TIM --host-url http://172.22.108.135:8086 --org TIM --token 8SuHJHSF74g_432i-CMi2GZRrOk-vUyOzkbuzpngg3pR8UAthP-vS0AEPCH72foK0dLb5kUjfGlLO2h94McT-w== --active

        Write-Output 'Config TIM generated'
    }
}

askforconfigfile
