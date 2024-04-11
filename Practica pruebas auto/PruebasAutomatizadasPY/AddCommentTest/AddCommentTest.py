from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from datetime import datetime
import sys

resultList = []
passed = 0
failed = 0

class AddCommentTest:
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
                
    def addComment(self):
        global failed
        global passed
        try:
            postOptions = self.driver.find_element(By.ID, "ReplyBtn")
            postOptions.click()
            self.driver.save_screenshot("./PruebasAutomatizadasPY/AddCommentTest/screenshot/step1_openoptions_submit.png")
            
            postOptions = self.driver.find_element(By.ID, "Content")
            postOptions.send_keys("Esto es un comentario de prueba")
            postOptions.submit()
            
            self.driver.save_screenshot("./PruebasAutomatizadasPY/AddCommentTest/screenshot/step2_AddComment_submit.png")
            passed += 1
            resultList.append(f"step add comment {datetime.now()} ")
        except Exception as e:
            failed  += 1
            resultList.append(f"Error while add coment {datetime.now()} ")
                
      
sys.path.append("C:\\Users\\hp\\Downloads\\Practica pruebas auto\\PruebasAutomatizadasPY\\ReportGenerator\\GeneratorReportFile")
from ReportGeneratorHtml import GeneratorReportHTML
        
def GenerateItsOwnReport():
    path = "./PruebasAutomatizadasPY/AddCommentTest/report/Report.html"
    
    generator = GeneratorReportHTML(path, resultList,failed,passed)
    generator.generate_report()
          

def run_test():
    try:
        screenshot_dir = './PruebasAutomatizadasPY/AddCommentTest/screenshot'
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
            

        
        login_test = AddCommentTest()
        login_test.step_start_sesion()
        print("Step 1: Login completed successfully.")
        login_test.addComment()
        print("Step 2: Step Make Comment completed successfully.")
        
    except Exception as e:
        print("Error during step:", e)
    finally:
        report_dir = './PruebasAutomatizadasPY/AddCommentTest/report'
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)    
                    
        GenerateItsOwnReport()
        login_test.driver.quit()

# Run the test
run_test()
