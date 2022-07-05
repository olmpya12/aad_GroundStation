from pymavlink import mavutil
import time

connection_strings = ["udpout:0.0.0.0:9000",""]

master = mavutil.mavlink_connection(connection_strings[0],force_connected=True)

master.wait_heartbeat()


def change_mode(mode):
    pass

def arm(force_arm=False):
    pass

def disarm():
    pass

def control_gimbal(tilt, roll=0, pan=0):
    pass

def set_servo(servo_no, value):
    pass

def read_gpio():
    pass


if __name__ == "__main__":
    while 1:
        pass
