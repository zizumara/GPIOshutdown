# GPIOshutdown
A Python script to initiate graceful shutdown on a Raspberry Pi by monitoring a GPIO pin

One vulnerability of the Raspberry Pi is its susceptibility to micro SD card corruption.  The main cause of this is interruption of power while the SD card is being written.  Such interruptions in some cases may not only corrupt the file being written, but may make the entire micro SD card unusable.  The problem is exacerbated in designs where the Raspberry Pi is run headless, leaving no convenient way to request a graceful shutdown.

The GPIOshutdown Python script, when run as a service, provides a way to initiate a graceful shutdown of the operating system by grounding one of its GPIO pins through a switch.  The script monitors pin 26 by default, but this may be changed by editing the value of SHUTDOWN_PIN in GPIOshutdown.py.  When launched, the script will wait for a fixed period before beginning to monitor the GPIO pin.  This is a fail safe to allow the user to login via SSH and stop the service to prevent continuous rebooting in the event that the GPIO pin is damaged or otherwise accidentally shorted.  The delay defaults to 180 seconds, but may be changed by editing the value of ARMING_DELAY IN GPIOshutdown.py.

Installation instructions are documented in setup.txt.
