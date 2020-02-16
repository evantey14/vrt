import serial, time, requests, threading 
ser = serial.Serial('/dev/ttyACM0', 9600)

azoff = 0
altoff = 0 
recalibrate = False 

def to_radians(x):
    return float(x)*3.14159/180

def calibrate_listener():
    global recalibrate
    kbdin = input("Type r to recalibrate:")
    if kbdin == 'r':
        recalibrate = True 
    else:
        calibrate_listener()

listener = threading.Thread(target=calibrate_listener)
listener.start()

while True:
    try:
        serial_line = ser.readline().decode('utf-8')
        coords = serial_line.split(',')
        print(coords)
        if recalibrate:
            recalibrate = False
            azoff = to_radians(coords[0])
            altoff = to_radians(coords[1]) - to_radians(90)
            listener = threading.Thread(target=calibrate_listener)
            listener.start()
        az = - to_radians(coords[0]) - azoff
        alt = to_radians(coords[1]) - altoff
        print(az, alt)
        requests.post('http://localhost:8090/api/main/view', 
                data={'az': az, 'alt': alt}) 
    except:
        pass

    time.sleep(.025) # less than the sensor rate because request takes time

ser.close()
