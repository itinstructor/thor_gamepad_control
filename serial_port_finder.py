# sys module to access system-specific parameters and functions
import sys
# glob module to find all the pathnames matching a specified pattern
import glob
# pyserial module to handle serial communication
# pip install pyserial
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):  # Check if the platform is Windows
        # Generate a list of COM ports
        ports = ['COM%s' % (i + 1) for i in range(256)]
    # Check if the platform is Linux or Cygwin
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # Find all the serial ports on Linux/Cygwin
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):  # Check if the platform is macOS
        ports = glob.glob('/dev/tty.*')  # Find all the serial ports on macOS
    else:
        # Raise an error if the platform is unsupported
        raise EnvironmentError('Unsupported platform')

    # Initialize an empty list to store the available serial ports
    result = []
    for port in ports:  # Iterate over the list of ports
        try:
            # Try to open the serial port
            s = serial.Serial(port)  
              # Close the serial port if it is successfully opened
            s.close()
              # Add the port to the result list if it was successfully opened
            result.append(port)
            
        except (OSError, serial.SerialException):  # Handle exceptions
            pass  # Ignore the exception and continue with the next port
    return result  # Return the list of available serial ports


if __name__ == '__main__':  # Check if the script is being run directly
    print(serial_ports())  # Print the list of available serial ports
