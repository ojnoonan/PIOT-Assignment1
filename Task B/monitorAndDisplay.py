from sense_hat import SenseHat
import json, os, time

b = (0,0,255) #blue
led_blue = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
]
g = (0,255,0) #green
led_green = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
]
r = (255,0,0) #red
led_red = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
]
sense = SenseHat()
sense.clear()

#setup loop to constatly check temps and update leds

# Get CPU temperature
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n",""))

# Get the file contents
def get_file_contents():
    readFile = open("Task B/config.json", "r")
    contents = readFile.read()

    data = json.loads(contents)

    for key, value in data.items():
        print(key, value)

def get_current_temp():
    # Get SenseHat temperature
    temp1 = sense.get_temperature_from_humidity()
    temp2 = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    
    # Get actual temperature
    t = (temp1+temp2)/2
    realTemp = t - ((t_cpu-t)/1.5)
    set_led(realTemp)

# Set led based on temp
def set_led(realTemp):
    print(realTemp)
    if realTemp <= 10:
        sense.set_pixels(led_blue)
    elif realTemp >= 25:
        sense.set_pixels(led_red)
    else:
        green = (255,0,0)
        sense.clear(green)
        #sense.set_pixels(led_green) 

get_file_contents()

while True: 
    get_current_temp()
    time.sleep(10)
