# Script Info
1. Generates rand(1,10) number of attendees per run.
2. Retrieves dummy data randomly from local file and inputs into field
3. Scripts shows the time spent and attendee info for the current run if success
4. Run configured script and have a coffee :coffee:

---

## Pre-requisites
1. Python
2. Basic CSS inspection skill via Web Developer Console
3. Create your own dummy data via [JSON Data Generator](https://mockaroo.com/)

---

## Installation Guide
1. Install Python 2.7
2. Download [Selenium WebDriver](http://chromedriver.chromium.org/getting-started)
   - Link WebDriver path into script
3. Enter event link   
   - Append #tickets as suffix
4. Enter login credentials (Email and Password)

---

## Customisation Guide
1. To get custom fields, right click inspect element and get the respective Field ID
   - e.g #id_attendee_5_first_name
2. Remove the iterator and replace it give str(i) as shown in script

---

## To-Do
[ ] Rename and tidy variables for easy config
[ ] Dynamic fields for any number of questions

---
## Terms
Be careful not to let the script run for too long as it will max out the number of attendees for that event with dummy data!

Please use this script **__ETHICALLY!__**

Strictly for testing and development purpose only!!

**__I am in no way responsible__** for any inconvenience or trouble YOU caused!
