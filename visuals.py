import time
import piglow
import pihole as ph


GREEN = 64
RED = 128
BLUE = 64
YELLOW = 128
ORANGE = 128

def check_status():
    if pihole.status == 'enabled':
        s = True
    else:
        s = False
    return s

def get_ads():
    num = int(pihole.blocked.replace(',', ''))
    return num


def flash_blue():
    # Turn off all, turn on red
    piglow.clear()
    piglow.blue(BLUE)
    piglow.show()
    # Leave on for 0.1 seconds
    time.sleep(0.2)
    
    # Leave off for 0.1 seconds
    piglow.clear()
    piglow.show()
    time.sleep(0.2)


def flash_green():
    # Turn off all, turn on green
    piglow.clear()
    piglow.green(GREEN)
    piglow.show()
    # Leave on for 0.1 seconds
    time.sleep(0.2)
    
    # Leave off for 0.1 seconds
    piglow.clear()
    piglow.show()
    time.sleep(0.2)
    
    
def flash_yellow():
    
    # Turn off all, turn on yellow
    piglow.clear()
    piglow.yellow(YELLOW)
    piglow.show()
    # Leave on for 0.1 seconds
    time.sleep(0.1)
    
    # Leave off for 0.1 seconds
    piglow.clear()
    piglow.show()
    time.sleep(0.1)
    
    
def flash_orange():
    
    # Turn off all, turn on red
    piglow.clear()
    piglow.orange(ORANGE)
    piglow.show()
    # Leave on for 0.1 seconds
    time.sleep(0.1)
    
    # Leave off for 0.1 seconds
    piglow.clear()
    piglow.show()
    time.sleep(0.1)
    
    
def flash_red():
    
    # Turn off all, turn on red
    piglow.clear()
    piglow.red(RED)
    piglow.show()
    # Leave on for 0.1 seconds
    time.sleep(0.1)
    
    # Leave off for 0.1 seconds
    piglow.clear()
    piglow.show()
    time.sleep(0.1)
    
    
def flash_all(): # Flashes all but blue
    flash_red()
    flash_orange()
    flash_yellow()
    flash_green()
    
    

# MAIN
# Create an object
pihole = ph.PiHole("10.0.0.2")
status = pihole.status
print("PiHole-PiGlow is " + status)

if status == 'enabled':
    enabled = True  
else:
    enabled = False
    
# Set the current ad count on startup
str_ads = pihole.blocked
ads = int(str_ads.replace(',', ''))

system_cycles = 0;
while enabled:
    
    for c in range(3): # Flash three times
        flash_green() # Signal start of refresh
        
    time.sleep(0.5)
    
    if system_cycles % 12 == 0: # ~2 minutes
        
        flash_all() # Signal Percentage Display
        percent = float(pihole.ads_percentage)  # Example: 31.2
        x = 0.0
        while x < percent:
            if x < percent - 10: 
                x += 10.0
                flash_blue() # 10%
            elif x < percent - 5:
                x += 5.0
                flash_orange() # 5%
            else:
                x += 1.0
                flash_yellow() # 1%
                
               
    refresh = get_ads() # Get the current number of ads blocked
    
    if refresh > ads:
        flash_yellow()
        flash_orange()
        while refresh > ads: # The refreshed number of ads is larger than tracked
            flash_red()     # Function Call, flash_red LED
            ads += 1        # Increment tracked ads
        flash_blue()
        flash_blue()
    
    # Idle for 10 seconds to reduce refresh rate
    time.sleep(10)
    system_cycles+=1
    
    pihole.refresh()
    enabled = check_status()

#When disabled show solid red
piglow.red(RED)
piglow.show()