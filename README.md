# hackedradiotrigger

I'm in the process of moving all of this info into a more git-friendly format, with specific code docs and higher res schematics.

Micro-controller controlled radio trigger

This project was originally designed as a wireless security alarm for a toilet seat (a surreal work assignment). The idea was that the alarm would go off whenever the toilet seat was lifted up. It’s based on hacking a radio trigger for a camera flash. The goal was to make the transmitter element as small, energy efficient, and water resistant as possible, while still allowing the battery to be changed easily.

This documentation is mostly complete, but I anticipate a future update to clarify certain parts, document the housing, and add better images, among other changes. The final version will likely be running on a Beagle Bone Black, instead of an Arduino Uno and a computer on the receiver side.

<strong>Possible Future Changes and Additions</strong><br>
-Remove unnecessary LEDs from trigger section to conserve battery.<br>
-Use DC barrel jack instead of screw terminals<br>
-Determine the behavior - should it ring once? Should it keep ringing until the seat is down again? etc.<br>
-Documentation of housing and switch mechanism will be added as it is developed.<br>
-Add an on/off switch to the transmitter battery.

<strong>Photo Flash Radio Trigger</strong><br>
This project uses a Vello FreeWave Mini-Stand Flash Trigger Set. Any non-TTL paired photo flash radio trigger set will work. If both elements are not designed for +3VDC power supplies, adjust as needed.
Both the transmitter and receiver of the radio trigger work by connecting the non-grounded trigger wire to ground. By connecting to ground, it was originally intended to short a capacitor in the flash, causing it to discharge. Both elements have 3 important contacts: +3VDC, ground, and trigger. The primary, non-TTL, contacts of a hot shoe are trigger and ground. The ground wire from the power supply can be wired into either the ground contact on the hotshoe or the battery compartment. The transmitter is triggered by connecting the trigger wire to ground. Similarly, when the receiver receives a radio pulse, it connects the trigger wire to ground.

<h3><strong>Parts</strong></h3><br>
Adafruit Pro Trinket 3V
Adafruit Pro Trinket Lilon/LiPoly Backpack
Lithium Ion Polymer Battery - 3.7v 500mAh
2x screw terminal
10K Ohm resistor
22 gauge solid core wire
3V Radio Trigger
Electrical contacts for button
Insulating material for button
Adhesive for button

<strong>Transmitter Power Consumption</strong>
Power supply: 500mAh Li-Po Battery

Adafruit Trinket
3.3V input
Amperage draw of Trinket (including LED): 9mA 
Amperage draw of “on” button: .3mA
Amperage of LED = 3mA
Total microcontroller draw with LED: 9.3mA
Total microcontroller draw without LED: 6.3mA

<strong>Amperage draw of Vello radio trigger</strong></br>
Vello Transmitter User Manual: https://static.bhphotovideo.com/lit_files/127128.pdf
Input Voltage: 3V 
Original Power Supply: CR2032
Battery life (in standby mode) with CR2032: 5yr
Typical CR2032 capacity: 220-240mAh
Estimated radio trigger draw (in standby mode): negligible
Estimated radio trigger draw (when triggered): slightly less negligible, but still negligible
Likely will work and draw even less power if the LED is removed. However, sometimes LEDs are needed as diodes as well as feedback to the user. Confirm before removing.
Total transmitter draw: negligible

<strong>Amperage draw of battery back pack</strong>
TBD

Total amperage draw without removing LEDs:  ~9.3

Battery Duration
500mAh/9.3mA= 54h
500mAh/6.3mA=79h

<h3><strong>Wiring</strong><h3>

Note: The default position is that the switch is closed. When the button is released (in this instance that means, when the toilet seat is lifted) it breaks the connection and triggers the alarm. Pin 8 (trigPin in the code) is set as an output. When it is set to LOW it is connected to ground. This is what enables the trigger to not use a relay.
