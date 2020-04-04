# PIOT-Assignment1
Programming Internet of Things Assignment 1 - Sense Hat

monitorAndDisplay.py
  The program stores the contents of the config.json into an array. 
  Functions In Program:
    - get_smooth()
        uses moving average to smooth readings given by the sense hat
    - get_cpu_temp()
        gets the temprature of the pi's CPU
    - get_file_contents()
        gets the contents contained within config.json, a try except block is used to catch any file errors
    - get_current_temp()
        gets the current temprature recoreded by the pi using the humidity and pressure sensors. It also takes into account           the temprature of the CPU
    - set_led()
        calls the get_current_temp() method and uses the returned result to run through an if statement. This will check if           the temprature meets the conditions mentioned in the file. It then displys the temprature in a scrolling text form             with the numbers colored based on the temprature.
game.py
  


Link to Git: https://github.com/s3660457/PIOT-Assignment1.git
