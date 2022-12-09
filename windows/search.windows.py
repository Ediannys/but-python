from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time
import subprocess
from collections import Counter

options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")

# using headless here means you are running the browser in the background
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#ensure your are using the right path and the chrome version is the same with your current chrome browser
driver = webdriver.Chrome(options=options)

stealth(driver,
    languages=["en-US", "en"],
    vendor= "Google Inc.",
    platform= "Win32",
    webgl_vendor= "Intel Inc.",
    renderer= "Intel Iris OpenGL Engine",
    fix_hairline=True
    )

queryList = []

try:
    with open("search.file.txt", "r") as file:
        if file.readable():
            words = file.read()
            queryList = words.split('\n')
            print (queryList)
            numberOfWords = len(queryList)

            if numberOfWords >= 1:
                try:
                    n_pages= int(queryList[0])
                    if isinstance(n_pages,int):
                        links=[]
                        titles=[]
                        listUrl = []
                        screen_height=driver.execute_script("return window.screen.height;")
                        queryList.pop(0) 

                        for query in queryList:
                            try:
                                print(query)
                                time.sleep(25)
                                for page in range(1, n_pages):
                                    url = "http://www.google.com/search?q=" + \
                                        query + "&start=" + str((page - 1) * 10)
                                    print(url)
                                    start = time.time()
                                    i = 0.01
                                    first = ""
                                    flagOPenFirst = False
                                    while True:
                                        time.sleep(1)
                                        end = time.time()
                                        count = round(end - start)
                                        if count == 5:
                                            driver.get(url)
                                            soup = BeautifulSoup(driver.page_source, 'html.parser')
                                            links = search = soup.find_all('div', class_="yuRUbf")
                                            first = links[0].a.get('href')
                                            print(first)
                                            time.sleep(10)
                                            driver.get(first)
                                            flagOPenFirst = True
                                            time.sleep(10)
                                        

                                        if flagOPenFirst == True:
                                            i += 0.1
                                            y = screen_height * i
                                            print ("Scrolling down i==" + i)
                                            driver.execute_script("window.scrollTo(0, {y});".format(y=y))
                                            
                                            if i >= 10:
                                                break
                                            
                            except Exception as e:
                                print(e)
                                print("Let me sleep for 10 seconds")
                                print("ZZzzzz...")
                                time.sleep(10)
                                print("Was a nice sleep, now let me continue...")
                                continue
                        driver.quit()
                except:
                    print("The first term of the list must be numeric, it represents the number of pages in the search")

            else:
                print("There must be at least one search term")
            
except Exception as e:
    print("Error opening the file" + e)