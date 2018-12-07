# Receipt Printer


# Table of Contents

- 1) Hardware
  - 1.1) Hardware Requirements
  - 1.2) Hardware Setup



# 1) Hardware

## 1.1) Hardware Requirements


### Main Processor
- 1 x Dragon Board 410C
- 1 x dragonboard sensor Mezzanine
- 1 x [12V 2A plug-in Adaptor](https://www.arrow.com/en/products/wm24p6-12-a-ql/autec-power-systems) (When purchases, comes with compatible power adaptor)
 
### Thermal Printer
- 1 x [Adafruit Thermal Printer Guts](https://www.adafruit.com/product/2753)
- 1 x [2.1mm Female DC Power adapter](https://www.adafruit.com/product/368) 
- 1 x [5V 2A power supply](https://www.adafruit.com/product/276) 
- 1 x [Nokia 5110 (PCD 8544)](https://www.adafruit.com/product/338)
  
### LCD Screen
- 1 x [PCD 8544 (Nokia 5110)](https://www.adafruit.com/product/338)
- 1 x [BSS138 4 Channel Bi-directional level shifter](https://www.adafruit.com/product/757) 
  
### Connector
  - 1 x USB to TTL Serial Cable
  - 1 x Breadboard 
  - 1 x 10k ohm resistor
  - 10 x male-female wire
  - 10 x male-male wire
  - 10 x female-female wire




## 1.2) Hardware Setup



### DragonBoard 410C Setup

Place the sensor Mezzanine on top, so it is fully covering the Dragonboard. Then connect the power adaptor on the Dragonboard to turn on.

IMPORTANT:
- DO NOT connect the Mezzanine while the Dragonboard is TURNED ON! It will short the circuit and break the board. 


### Thermal Printer Setup
  
First, screw two wires (positive and negative) on to the Female DC power adaptor. Connect the positive port to the VH pin of the printer. Connect the ground to the GND pin. 

For more detailed instructions of how to hook up the thermal printer, look into [here](https://learn.adafruit.com/mini-thermal-receipt-printer/microcontroller) (labeled as product #2753) 


IMPORTANT:
- The ground pin from the power adaptor must also be connected to the ground pin of the Dragon Board
- Your power adaptor needs to supply at least 1.5A at 5V. Thermal printer requires a lot of power!

Since we used a USB Serial Port, we simply connect the USB port of the board to the USB connector. 

| USB Serial Port  | Thermal Printer |
| ------------- | ------------- |
| RX  | TX  |
| TX  | RX  |

IMPORTANT:
- We connected the TX and the RX opposite from what the USB Serial Port has labeled in order for it to work. However, this is highly unlikely for other cases. 
- J1 on the PCB acts as a reset button. Just use a wire to short them when you want to use the button feature. 


### LCD Screen Setup

The LCD screens needs 3.3V, which is not supplied from the Dragonboard. (1.8V and 5V only) There are three ways to connect the LCD. First, use the 3.3V pins from the Mezzanine board to connect to the LCD screen. Second, use only 3.3V pin and Ground to use it for the reference for level shifter. Third, from the 5V of Dragonboard, simply create a voltage divider circuit to drop the voltage from 5V to 3.3V. 

The first option would be the best choice. However, the team did not have enough time to do proper research on the sensor Mezzanine to have a full understanding of how to use the 3.3V signal pins. So, we decided to stick with second option. The third option does not establish a proper connection between the LCD and the board. It works for now, but might run into problems when the component is changed to something that requires more power. 

For more hookup guide, look into [Sparkfun’s Level Convertor hookup guide](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all). (Although it’s from Sparkfun, it works well with any level shifter)


The High Voltage side is connected to the Dragonboard

| Dragonboard  | Thermal Printer |
| ------------- | ------------- |
| GND (pin 2)  | GND  |
| 5V  | HV  |
| Pin 8  | B1 |
| Pin 14  | B2  |
| Pin 24 | B3  |
| Pin 26  | B4  |
| 3.3V | LV  |

One thing to note is that the GND of HV and LV side need to be wired. 


To connect the Level shifter to LCD screen, 

| Level Shifter | LCD Screen |
| ------------- | ------------- |
| GND  | GND  |
| LV | VCC  |
| A1  | CLK  |
| A2  | DIN  |
| A3  | D/C  |
| A4  |  CS |
| 3.3V from Board |  RST |
| NC  | LED  |

You should place 10k ohm resistor betwwen the 3.3V from the board and RST.
CLK and DIN must be Clock and Serial Data In (MOSI) respectively, but D/C and CS can be any GPIO Pin. Note that RST is connected directly to the board meaning it is always stated HIGH. The LCD cannot use it’s RESET purpose, but it works, so don’t worry!


# 2) Software

## 2.1) Build Environment Setup

We used Debian Linaro for this project, instructions can be [found here](https://www.96boards.org/documentation/consumer/dragonboard/dragonboard410c/downloads/debian.md.html)

## 2.2) Dependencies

## 2.3) Modules and Libraries

## 2.4) Code

# 3) Setting up TRON Wallet


