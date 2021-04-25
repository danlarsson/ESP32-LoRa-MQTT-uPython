from config import *
from machine import Pin, SoftSPI
from sx127x import SX127x
from time import sleep
import display

# Setup LoRa
device_spi = SoftSPI(baudrate = 10000000,
        polarity = 0, phase = 0, bits = 8, firstbit = SoftSPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

def send():
    lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)
    print("LoRa Transmitter")
    counter = 0

    while True:
        payload = 'Number %i' % counter
        print("Sending packet: \n{}\n".format(payload))
        display.display('LoRa TX', payload)
        lora.println(payload)
        lora.blink_led()

        counter += 1
        sleep(5)


def recive():
    lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)
    print("LoRa Receiver")

    while True:
        if lora.received_packet():
            lora.blink_led()
            print('Receiving packet')
            payload = lora.read_payload()
            rssi = lora.packet_rssi()
            snr = lora.packet_snr()
            
            print(payload)
            print('Rssi: %i' % rssi)
            print('SNR: %i' % snr)
            display.display('LoRa RX', payload, snr, rssi)


if __name__ == '__main__':
    recive(lora)
	# send(lora)

