import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
from selenium.common.exceptions import NoAlertPresentException

import json
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)

def spamAttendees(self):
    options = Options()

    # remove comments below if you want to watch Automation in action
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")

    # Add your path to webdriver here
    # http://chromedriver.chromium.org/getting-started
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path="")
    # print("Chrome Headless Browser Invoked")
    condition = 0
    numOfParticipants = randint(1,10)

    for spam in range(randint(1, 800),1000,10):
        try:
            print "New instance!"

            # Add your event path here with #tickets as suffix
            # e.g "event-name-EVENTID#tickets"
            # path = "zoukout-2018-46831234567#tickets"
            httpLink = "https://www.eventbrite.com/e/"
            path = ""

            url = httpLink + path
            driver.get(url)
            time.sleep(3)
            # select_fr = Select(driver.find_element_by_class_name("ticket-box-quantity"))
            select_fr = Select(driver.find_element_by_id("quant_87679601_None"))
            select_fr.select_by_index(numOfParticipants - 1)
            time.sleep(3)
            driver.find_element_by_xpath(".//button[contains(text(), 'Checkout')]").click()
            # Login
            if (condition == 0):
                driver.find_element_by_xpath(".//a[contains(text(), 'Sign In To Your Account')]").click()

                loginEmail = driver.find_element_by_css_selector("#loginForm #email")
                # Add your login credentials here
                loginEmail.send_keys("")

                loginPassword = driver.find_element_by_css_selector("#loginForm #passwd")
                # Enter your password
                loginPassword.send_keys("")

                driver.find_element_by_css_selector("#loginForm span.go_button").click()
                print "Signed in!"
            startTime = datetime.now()
            attendeesInfo = ""
            # Fields
            for i in range(1,numOfParticipants+1):

                #First Name
                fNameField = driver.find_element_by_css_selector("#id_attendee_"+str(i)+"_first_name")
                fNameField.send_keys(data[spam+i]["First name"])

                # Last Name
                lNameField = driver.find_element_by_css_selector("#id_attendee_" + str(i) + "_last_name")
                lNameField.send_keys(data[spam+i]["Last name"])

                # Email
                emailField = driver.find_element_by_css_selector("#id_attendee_" + str(i) + "_email_address")
                emailField.send_keys(data[spam+i]["Email"])

                # Cell Phone
                phoneField = driver.find_element_by_css_selector("#id_attendee_" + str(i) + "_cell_phone")
                phoneField.send_keys(data[spam+i]["Cell phone"])

                #Gender
                select_gender = Select(driver.find_element_by_id("id_attendee_" + str(i) + "_sex"))
                select_gender.select_by_index(randint(1, 3))

                # Nationality
                select_nationality = Select(driver.find_element_by_id("id_attendee_" + str(i) + "_ans19287709"))
                select_nationality.select_by_index(randint(1, 6))

                # Working Experience
                select_experience = Select(driver.find_element_by_id("id_attendee_" + str(i) + "_ans19287727"))
                select_experience.select_by_index(randint(1, 5))

                # Which Field are you interested in?
                select_field = Select(driver.find_element_by_id("id_attendee_" + str(i) + "_ans19287728"))
                select_field.select_by_index(randint(1, 8))
                # print "Filled JSON " + str(spam+i) + " with " + str(i)
                attendeesInfo = attendeesInfo + \
                       "\nData entered:\n" + \
                       (data[spam+i]["First name"]) + " " +(data[spam+i]["Last name"]) + \
                       "\n" + (data[spam + i]["Email"] + "\n")
            # Submit all 10 fields
            driver.find_element_by_xpath(".//a[contains(text(), 'Complete Registration')]").click()
            time.sleep(3)
            endTime = datetime.now()
            timeTaken = endTime - startTime
            print "**********"
            # print "No: " + str(spam)
            print "Time taken: " + str(timeTaken.seconds) + " seconds"
            print "**********"

            if (i == numOfParticipants):
                condition = 1
                endTime = datetime.now()
                try:
                    popup = driver.switch_to.alert
                    popup.accept()
                    print "Error on " + str(spam+1) + " to " + str(spam + numOfParticipants)
                    driver.quit()
                    spamAttendees(self)
                except NoAlertPresentException as e:
                    print "Success!"
                    print attendeesInfo
                    driver.quit()
                    spamAttendees(self)

            timeTaken = endTime - startTime
            print "**********"
            print "No: " + str(spam)
            print "Time taken: " + str(timeTaken.seconds) + " seconds"
            print "**********"
            driver.quit()
            spamAttendees(self)
            # time.sleep(5)
        except:
            condition = 0
            print "Error!"
            spamAttendees(self)

spamAttendees(self=1)
