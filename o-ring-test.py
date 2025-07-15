# Material test for O-Ring, using a Prusa 3D Printer with G-code Commands
# This script sends G-code commands to a 3D printer via a serial connection.
# Make sure to have the 'pyserial' library installed: pip install pyserial

import serial
import time
# === Configuration ===
port = '/dev/ttyUSB0'  # Change this to your serial port, e.g., 'COM3' on Windows
baudrate = 115200      # Most 3D printers use 115200 or 250000 baud
feedrate = 3000        # Movement speed
delay_between_moves = 0.1  # seconds between commands
# === Initialize Serial Connection ===
ser = serial.Serial(port, baudrate, timeout=1)
time.sleep(2)  # Wait for the printer to initialize
# === Send initialization commands ===
ser.write(b"G90\n")  # Use absolute positioning
ser.write(b"G21\n")  # Set units to millimeters
time.sleep(1)
ser.write(b"G28\n") # return to home position
time.sleep(5)  # Wait for homing to complete
# === Generate and send movements ===
for i in range(100):
    for x in range(0, 21):  # X0 to X20
        gcode = f"G1 X{x} F{feedrate}\n"
        print(f"Sending: {gcode.strip()}")
        ser.write(gcode.encode())
        time.sleep(delay_between_moves)
# === Finish ===
print("Finished sending all movements.")
ser.close()