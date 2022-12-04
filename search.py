from selenium import webdriver 
import time
import subprocess
list = ["Tesla Motors", "Canadá", "Brasil", "Colombia"]

# Use Chrome Explorer to simulate
driver = webdriver.Chrome() 
tabUrl="https://www.google.com/search?q="

# Execute the scroll order by webdriver
screen_height=driver.execute_script("return window.screen.height;") 



for pos in range(len(list)):
    start = time.time()
    i = 1
    term=list[pos]
    p = subprocess.Popen("gnome-terminal -e 'protonvpn-cli c -r'", stdout=subprocess.PIPE, shell=True)
    print(p.communicate())

    if p.returncode == 0:
        print ('command: success')
        while True:
            time.sleep(1)
            end = time.time()
            count = round(end - start)
            print(count)

            if count == 20:
                driver.get(tabUrl+term)

            if count > 22:
                i += 0.1
                driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
               
            if count > 80:
                break
    else:
        print('command: failed')


        
p = subprocess.Popen("gnome-terminal -e 'protonvpn-cli disconnect'", stdout=subprocess.PIPE, shell=True)
print(p.communicate())
      