from sense_hat import SenseHat
import json, os, time

sense = SenseHat()
sense.clear()

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)

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
    realTemp = get_smooth(realTemp)
    set_led(realTemp)

# Set led based on temp
def set_led(realTemp):
    print(realTemp)
    if realTemp <= 10:
        b = (0,0,255) #blue
        sense.clear(b)
        #sense.set_pixels(led_blue)
    elif realTemp >= 25:
        r = (255,0,0) #red
        sense.clear(r)
        #sense.set_pixels(led_red)
    else:
        g = (255,0,0) #green
        sense.clear(g)
        #sense.set_pixels(led_green) 

get_file_contents()

while True: 
    get_current_temp()
    time.sleep(10)
