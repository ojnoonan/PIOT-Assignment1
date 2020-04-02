from sense_hat import SenseHat
import json, os, time

sense = SenseHat()
sense.clear()

file_contents = [] #storing the current file contents

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
    try:
        readFile = open("config.json", "r")
        contents = readFile.read()

        data = json.loads(contents)
    
        file_contents.clear() #clear the array for existing data
        for value in data.items():
            file_contents.append(value) #storing updated file contents
    except OSError as e:
        print("File not found")
        print(e)

def get_current_temp():
    # Get SenseHat temperature
    temp1 = sense.get_temperature_from_humidity()
    temp2 = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    
    # Get actual temperature
    t = (temp1+temp2)/2
    realTemp = t - ((t_cpu-t)/1.5)
    realTemp = get_smooth(realTemp)
    # set_led(realTemp)
    return realTemp

# Set led based on temp
def set_led():
    colour = (255,255,255)
    realTemp = get_current_temp()
    if realTemp <= file_contents[0]:
        colour = (0,0,255) #blue
        # sense.clear(b)
    elif realTemp >= file_contents[3]:
        colour = (255,0,0) #red
        # sense.clear(r)
    else:
        colour = (255,0,0) #green
        # sense.clear(g)
    sense.show_message(round(realTemp), text_colour=colour)

while True:
    get_file_contents()
    get_current_temp()
    time.sleep(10)