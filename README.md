# RC522-RFID-with-RPi
RC522 RFID connects with Raspberry Pi to read and write MIFARE tags and Card. It basically used for Security Purpose. Must seen in college ID card,when it detect a valid person then only allow inside premises.

## RFID(Radio Frequency Identification)

- The device is based on the Radio frequency signals.
- The RFID systems consists of RFID Reader and a tag which is normally used in identification and tracking of objects.
- It is a device which consists of an antenna, transceiver and a decoder.
- Radio-Frequency Identification (RFID) is the use of radio waves to read and capture information stored on a tag attached to an object.

![alt text](https://github.com/Anmol17Agarwal/RC522-RFID-with-RPi/blob/main/RFID.jpg)

## Serial Communication UART

- UART (Universal Asynchronous Transmitter Receiver), this is the most common protocol used for full-duplex serial communication. 
- It is a single LSI (large scale integration) chip designed to perform asynchronous communication. 
- This device transmit and receives data from one system to another system which done by cross connection and either transmit or recieves data from one to another system by singe connection.

![alt text](https://github.com/Anmol17Agarwal/RC522-RFID-with-RPi/blob/main/UART-Block-Diagram.webp)

## Equipment Requirement

- Raspberry Pi 3
- Micro SD card
- RC522 RFID
- RFID tag or Card
- BreadBoard
- Jumper Wires
- Power Supply

## Wiring to RC522 RFID
- SDA -------->GPIO8.
- SCK -------->GPIO11.
- MOSI -------->GPIO10.
- MISO -------->GPIO9.
- GND -------->Gnd.
- RST -------->GPIO25.
- 3.3v -------->3.3v.

![alt text](https://github.com/Anmol17Agarwal/RC522-RFID-with-RPi/blob/main/Raspberry-Pi-RC522%20connection.png)

## Setting Up

Before setting up RC522 in Raspberry Pi, first make changes in configuration.
1. Open Raspian Command Prompt and run the following Command.
```
sudo raspi-config
```
2. This will open a screen and shows different option. Select 5 INTERFACING OPTION > P4 SPI and press enter. It will ask to allow SPI interface Press YES.

3. Now restart the Raspberry Pi by reboot it.
```
sudo reboot
```
4. Once it get rebooted,Again open and install pip library of spidev in your Rpi by following commands. Where sudo means System User do and pip3 means python version 3.
``` 
sudo install pip3 spidev
```
5. There are two files that are included within our MFRC522 library that we make use of:MFRC522.py which is an implementation of the RFID RC522 interface, this library handles all the heavy lifting for talking with the RFID over the Pi’s SPI Interface.SimpleMFRC522.py that takes the MFRC522.py file and greatly simplifies it by making you only have to deal with a couple of functions instead of several.To install the MFRC522 library to your Raspberry Pi using pip go ahead and run the following command.

```
sudo install pip3 mfrc522
```
6. Now All libraries are install in your RaspberryPi and run your Python program.

#### Writing RFID RC522

Run the rfWriteRC522.py code and simply store your details in RFID card in try block. Clear all data from RPi in finally block, so that next details can be registered in next RFID card.

#### Reading RFID RC522

Run the rfReadRC522.py code and simply read all the details which store in RFID card.

### Connection of Hardware

![alt text](https://github.com/Anmol17Agarwal/RC522-RFID-with-RPi/blob/main/Hardware%20connection.jpg)
