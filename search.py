from selenium import webdriver 
import time
list = ["Tesla Motors", "Canadá", "Brasil", "Colombia"]
term=list[0]
# Use Chrome Explorer to simulate
driver = webdriver.Chrome() 
tabUrl="https://www.google.com/search?q="
# Get the sample website to be scrolled
driver.get(tabUrl+term) 

# Execute the scroll order by webdriver
screen_height=driver.execute_script("return window.screen.height;") 

i = 1
# Record the starting time of the loop
start = time.time()
while True:
    # Scroll 1 screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 0.1
    # Allow for pause time to load data
    time.sleep(1)
    # Record ending time of the whole loop
    end = time.time()
    # Break the loop with a given time limit
    if round(end - start) > 30:
        break