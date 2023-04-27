Folder 'influx' must be in C:\Program Files\InfluxData\

commands here: https://docs.influxdata.com/influxdb/cloud/reference/cli/

Create config file, set --host-url to active and upload data:
1) PS C:\Program Files\InfluxData\influx> .\influx config create --config-name TIM --host-url http://172.22.108.135:8086 --org TIM --token 8SuHJHSF74g_432i-CMi2GZRrOk-vUyOzkbuzpngg3pR8UAthP-vS0AEPCH72foK0dLb5kUjfGlLO2h94McT-w== --active
2) PS C:\Program Files\InfluxData\influx> .\influx write --bucket TestKlaus_from_DesktopPC --format=csv --file C:/tmp/test_formatted.csv

Further improvements for automatization:
1) Ask if bucket exists; if not, create new bucket: https://docs.influxdata.com/influxdb/cloud/reference/cli/influx/bucket/

2) Ask if config file exists; if not, delete/create new one: https://docs.influxdata.com/influxdb/cloud/reference/cli/influx/config/