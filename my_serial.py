from serial import Serial
from threading import Thread

s0 = Serial()
s0.port = "/dev/ttyACM0"
s0.baudrate = 115200
s0.timeout = 1
s0.close()
s0.open()


def serial_read():
    while True:  # keeps open the serial interface
        if not s0.is_open:
            break
        try:
            s0.in_waiting
        except Exception as e:
            print("SERIAL-DISCONNECTED")
            print("Lost Serial connection!")
            print(e)
        try:
            s0.readline()
        except Exception as e:
            print("Something failed: " + str(e))


def serial_write(cmd):
    cmd = cmd + "\n"
    s0.write(cmd.encode("UTF-8"))


read_thread = Thread(target=serial_read)
read_thread.daemon = True  # will be closed when not used

if __name__ == "__main__":
    print("Run control.py instead")
