# igloo
Central Heating Controller on Raspberry Pi (like nest and hive, only better)

This heating controller consists of:
* A RPi with WiFi and a small PSU and relay on the wall where the thermostat used to be. 
* Lots of LM35 thermometers in different rooms, in the garden and behind radiators, dangled along some alarm wire.
* Some programming ingenuity

Build HW:
* Connect one LM35 to the RPi via MCP3008 ADCs, read and calibrate.
* Try that at the end of 100m of alarm wire and develop damping capacitors etc. 
* Graph over 24 hours to check it works.
* Install all wiring: 16 LM35s over 2 ADCs, Pi in its box. Thermo units should be unclippable along the wires.
* Get the relay working like a clockwork thermostat.
* Persistently graph everything.

* Check that brief bursts on the relay can run boiler's pump without gas indefinitely. Fine tune.
* All radiator valves wide open: inject pulse of heat, overrun pump, watch heatwave travel around radiators. Not ordering of radiators. 
* Hope wave stays sharply defined for a while:
  * If so, choose "heatwave" strategy: aim bubbles of hot water at specific radiators
	* If not, choose "mixer" strategy: unbalance radiators and overrun to mix back to evenness.
	* Or buy solenoid valves and deploy more wire.
	* Or just balance radiators using room thermometers.

The garden thermometer is very important. Hive reads the outside temp off the weather forecast - perhaps that's OK too. It also has a motion sensor to learn when you go out and come back.
You can get little heatsinks to attach to the LM35s for faster response.

We need some function returning target temperature by time and place. It should support "don't care". It needs a civilised way to edit it.
Then we have to learn to aim for the target. There's PID style, or there's ...

Model the house as a bunch of rooms each with a heat capacity and a radiator and a conductance to each other room including the garden.
Looking at the radiator and room temperatures, we can get all the parameters of that model over time.
Then we need a model of the radiator pipes. We learn that by playing with the relay and watching the radiator temperatures.

TBC


Cookbook:

* http://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/

