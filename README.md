Tetrahedrally Truncated Dodecahedron Clock
==================
A clock built using a Raspberry Pi, LED seven segment and dot matrix displays driven by MAX7219. The python code uses the excellent MAX7219 driver by Richard Hull https://github.com/rm-hull/max7219

The code is simple and displays local/UTC time, and time-based one-time password for a 2-Step verification account.

![Tetrahedrally Truncated Dodecahedron](https://raw.githubusercontent.com/sharjeelaziz/dodecahedron-clock/master/front-view.jpg)

[![Dodecahedron Clock](http://img.youtube.com/vi/-RI2aG52GX4/0.jpg)](http://www.youtube.com/watch?v=-RI2aG52GX4)

Pre-requisites
--------------
Ensure that the SPI kernel driver is enabled:

  pi@raspberrypi ~ $ dmesg | grep spi
  [    6.164368] bcm2708_spi 20204000.spi: master is unqueued, this is deprecated
  [    6.489381] bcm2708_spi 20204000.spi: SPI Controller at 0x20204000 (irq 80)

And that the devices are successfully installed in /dev:

  pi@raspberrypi ~ $ ls -l /dev/spi*
  crw-rw---T 1 root spi 153, 0 Dec 31  1969 /dev/spidev0.0
  crw-rw---T 1 root spi 153, 1 Dec 31  1969 /dev/spidev0.1

Refer to http://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md if the devices do not appear before proceeding.

GPIO pin-outs
-------------
The breakout board has an two headers to allow daisy-chaining:

| Board Pin | Name | Remarks | RPi Pin | RPi Function |
|--------:|:-----|:--------|--------:|--------------|
| 1 | VCC | +5V Power | 2 | 5V0 |
| 2 | GND | Ground | 6 | GND |
| 3 | DIN | Data In | 19 | GPIO 10 (MOSI) |
| 4 | CS | Chip Select | 24 | GPIO 8 (SPI CS0) |
| 5 | CLK | Clock | 23 | GPIO 11 (SPI CLK) |

Case
====
The case is designed in SketchUp. Printed at ShapeWays in [White Strong & Flexible](https://www.shapeways.com/materials/strong-and-flexible-plastic?li=nav) material and is available at http://shpws.me/Im4Y

Display
=======
Displays are sourced from ebay and below are some helpful searches:

* [MAX7219 Red Module 8-Digit 7 Segment Digital LED Display](http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.TRS0&_nkw=MAX7219+Red+Module+8-Digit+7+Segment+Digital+LED+Display&_sacat=0)
* [max7219 dot matrix module](http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2047675.m570.l1311.R5.TR7.TRC2.A0.H0.XMAX7219+.TRS1&_nkw=max7219+dot+matrix+module&_sacat=0)


References
----------
* https://github.com/rm-hull/max7219
* http://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md

License
-------
Copyright 2015 Sharjeel Aziz (Shaji)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Dodecahedron Clock</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://sharjeelaziz.github.io" property="cc:attributionName" rel="cc:attributionURL">Sharjeel Aziz (shaji)</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
