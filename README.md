# E-Paper HAT Module Documentation

## Version Information
- Version: V1.0
- Date: 2021-06-05
- Purpose: Quick start guide for English users

## Basic Information
This demo was verified on Raspberry Pi 4B using the XXXinch e-paper HAT module.
You can find the corresponding test routines in the `\lib\Examples\` directory of the project.

## Pin Connections
The following connections can be found in `\lib\epdconfig.py`:

| EPD Pin | Jetson Nano/RPI(BCM) |
|---------|---------------------|
| VCC     | 3.3                |
| GND     | GND                |
| DIN     | 10 (SPI0_MOSI)     |
| CLK     | 11 (SPI0_SCK)      |
| CS      | 8 (SPI0_CS0)       |
| DC      | 25                 |
| ERST    | 17                 |
| BUSY    | 24                 |
| INT     | 27                 |
| TRST    | 22                 |
| SDA     | SDA1               |
| SCL     | SCL1               |

## Installation Requirements

### Python 2
```bash
sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install python-pil
sudo apt-get install python-numpy
sudo pip install RPi.GPIO
sudo pip install spidev
```

### Python 3
```bash
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
```

## Basic Usage
Since this project is a comprehensive project, you may need to read the following for use:
- You can view the test program in the `examples\` directory
- Please note which ink screen you purchased

### Example
If you purchased 2.9inch Touch e-Paper HAT, then you should execute the command:
```bash
sudo python TP2in9_test.py
```
or
```bash
sudo python3 TP2in9_test.py
```