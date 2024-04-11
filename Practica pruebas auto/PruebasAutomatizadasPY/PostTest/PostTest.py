from selenium import webdriver
from selenium.webdriver.common.by import By
import os

import sys


from datetime import datetime
import sys



resultList = []
passed = 0
failed = 0


class Make_Post:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get("https://localhost:44382/")
            global passed
            global failed
            
            # Wait for the login page to fully load
            self.driver.implicitly_wait(10)
            resultList.append(f"Application started sucessfully {datetime.now()} ")
            passed += 1
        except Exception as e:
            failed  += 1
            resultList.append(f"Error while starting app {datetime.now()} ")
                
        
    

    def step_start_sesion(self):
        global passed
        global failed
        
        try:
            # Take a screenshot after the login page has loaded
            self.driver.save_screenshot("./PruebasAutomatizadasPY/PostTest/screenshot/step1_login_page.png")
            # Enter valid credentials
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("Coquito1010")
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("@Coquito1010")
            password_field.submit()
            # Take a screenshot after submitting the credentials
            self.driver.save_screenshot("./PruebasAutomatizadasPY/PostTest/screenshot/step1_login_submit.png")
            resultList.append(f"Login user sucessfully {datetime.now()} ")
            passed += 1
        except Exception as e:
            failed  += 1
            resultList.append(f"Error while login user {datetime.now()} ")
            
        
    def step_MakePost(self):
        global passed
        global failed
        
        try:
            postText = self.driver.find_element(By.ID, "Caption")
            postText.send_keys("Esto es un post de prueba")
            postText.submit()
            self.driver.save_screenshot("./PruebasAutomatizadasPY/PostTest/screenshot/step2_Makepost.png")
            resultList.append(f"step_MakePost was done sucessfully {datetime.now()} ")
            passed += 1
        except Exception as e:
            failed += 1
            resultList.append(f"Error while step_MakePost {datetime.now()} ")
          
sys.path.append("C:\\Users\\hp\\Downloads\\Practica pruebas auto\\PruebasAutomatizadasPY\\ReportGenerator\\GeneratorReportFile")
from ReportGeneratorHtml import GeneratorReportHTML
        
def GenerateItsOwnReport():
    path = "./PruebasAutomatizadasPY/PostTest/Report/Report.html"
    
    generator = GeneratorReportHTML(path, resultList,failed,passed)
    generator.generate_report()
    
        
           
        
      
        

def run_test():
    try:
      screenshot_dir = './PruebasAutomatizadasPY/PostTest/screenshot'
      if not os.path.exists(screenshot_dir):
           os.makedirs(screenshot_dir)
           

           
        
      post_test = Make_Post()
      post_test.step_start_sesion()
      print("Step 1: Login completed successfully.")
      post_test.step_MakePost()
      print("Step 2: Step Make Post completed successfully.")
      
      
    except Exception as e:
        print("Error during step:", e)
    finally:
      report_dir = './PruebasAutomatizadasPY/PostTest/report'
      if not os.path.exists(report_dir):
           os.makedirs(report_dir)    
                   
      GenerateItsOwnReport()
      post_test.driver.quit()

# Run the test
run_test()
