import display
import network

sta_if = network.WLAN(network.STA_IF)
ip = sta_if.ifconfig()[0]

display.display('LoRa GW', ip)

print('Hello fellow Ham')
print('Start with:')
print('import LoRa')
print('LoRa.send()    or   LoRa.recive()')

