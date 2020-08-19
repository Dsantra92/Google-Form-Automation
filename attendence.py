import urllib.parse
import webbrowser                  #For forms having recaptcha.We are opening it through the browser.
import datetime

def get_PeriodName_Time(day, period_no):

        subjects = ["Mathematics & Statistics III (BSM301)","Electronic Devices (PCC-EC301)",
                    "Analog Electronic Circuits (PCC-EC302)","Network Theory (PCC-EC303)",
                    "Signal & System (PCC-EC304)", "Essential Studies for Professionals III (HUSS-ESP-301)",
                    "Biology for Engineers (MC301)","Electronic Devices & Analog Circuits Lab (PCC-EC391)",
                    "Signals & Systems Lab (PCC-EC394)","Data Structure and Algorithm (Sessional) (OEC-EC381)",
                    "Skill Development for Professionals III (HUSS-SDP- 381)","PROJECT I (ECP-381)"]


        routine = [[0, 2, 1, 2, 8, 8],
                   [9, 9, 4, 0, 5, 4],
                   [3, 0, 2, 7, 7,10],
                   [4, 6,10, 1, 3, 2],
                   [4, 3, 6, 1, 6, 5]]

        period_theory_timings = ["1st (9.30 am - 10.20 am)","2nd (10.30 am - 11.20 am)",
                                 "3rd (11.30 am - 12.20 am)","4th (1.10 pm - 2.00 pm)",
                                 "5th (2.10 pm - 3.00 pm)","6th (3.10 pm - 4.00 pm)"]


        period_lab_timings = {1 : "Lab Class (1st - 2nd Period)",
                              4 : "Lab Class (4th - 5th Period)",
                              5 : "Lab Class (5th - 6th Period)"}
        
        time = period_theory_timings[period-1]
        
        if period <= 5 :
                if routine[day][period-1] == routine[day][period] :
                        time = period_lab_timings[period]
        if period >= 2 :
                if routine[day][period-1] == routine[day][period-2] :
                        time = period_lab_timings[period]


        return (subjects[routine[day][period-1]],time)


url = "https://docs.google.com/forms/d/e/1FAIpQLSebcakSCz135JZoO5CRKfc_918qKVoqVUi2jprVKrLaTebZrg/" + "formResponse?&pageHistory=0,1&"

#Edit you personal details.

name = "<ENTER YOUR NAME HERE>"
email = "<ENTER YOUR EMAIL ID HERE>"
roll = "<ENTER YOUR ROLL NUMBER HERE>"

section = "A"
year = "2nd Year"
date = datetime.date.today().isoformat()
day = datetime.datetime.today().weekday()
period = int(input("Enter the preiod of the day : "))
period_name, period_time = get_PeriodName_Time(day,period)


data = {"entry.1815716569":name, "entry.1692281654" : section, 
        "emailAddress" : email, "entry.1893750295" : roll,
        "entry.1931187150" : date, "entry.1031915049" : period_time,
        "entry.888269602":year,"entry.1907638825" : period_name}



response = urllib.parse.urlencode(data)

user_response = url + response

#If there is an error regarding browser.uncomment the next line and add browser path

#webbrowser.get(<address of the your broswer execution file>).get(user_response)
try:
    webbrowser.open(user_response)
except:
    print("An error occoured")
