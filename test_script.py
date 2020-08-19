import urllib.parse
import urllib.request
import datetime

def get_PeriodName_Time(day, period_no):

        subjects = ["Mathematics & Statistics III (BSM301)","Electronic Devices (PCC-EC301)",
                    "Analog Electronic Circuits (PCC-EC302)","Network Theory (PCC-EC303)",
                    "Signal & System (PCC-EC304)","Essential Studies for Professionals III (HUSS-ESP-301)",
                    "Biology for Engineers (MC301)", "Electronic Devices & Analog Circuits Lab (PCC-EC391)",
                    "Signal & Systems Lab (PCC-EC394)","Data Structure and Algorithm (Sessional) (OEC-EC381)",
                    "Skill Development for Professionals III (HUSS-SDP- 381)","PROJECT I (ECP-381)"]

        routine = [[0, 2, 1, 2, 8, 8],
                   [9, 9, 4, 0, 5, 4],
                   [3, 0, 2, 7, 7,10],
                   [4, 6,10, 1, 3, 2],
                   [4, 3, 6, 1, 6, 5]]

        period_theory_timings = ["1st (9.30am - 10.20am)", "2nd (10.30am - 11.20am)",
                                 "3rd (11.30am - 12.20pm)","4th (1.10pm - 2.00pm)",
                                 "5th (2.10pm - 3.00pm)","6th (3.10pm - 4.00pm)"]


        period_lab_timings = {1 : "Lab Class (1st-2nd Period)",
                              4 : "Lab Class (4th-5th Period)",
                              5 : "Lab Class (5th-6th Period)"}
        
        time = period_theory_timings[period-1]
        
        if period <= 5 :
                if routine[day][period-1] == routine[day][period] :
                        time = period_lab_timings[period]
        if period >= 2 :
                if routine[day][period-1] == routine[day][period-2] :
                        time = period_lab_timings[period]


        return (subjects[routine[day][period-1]],time)



url = "https://docs.google.com/forms/d/e/1FAIpQLScf-ISET-XOiEBDyRtpuWIz4S98iC6Nzq247OgIAo4Dvs6vlA/" + "formResponse?&pageHistory=0,1&"



email = "santradibbo@gmail.com"
name = "Deeptendu Santra"
section = "A"
roll = "9"
date = datetime.date.today().isoformat()
day = datetime.datetime.today().weekday()
period = int(input("Enter the preiod of the day : "))
period_name, period_time = get_PeriodName_Time(day,period)




data = {"entry.375405198":name, "entry.1748177020" : section, 
        "emailAddress" : email, "entry.1479767868" : roll,
        "entry.1691501242" : date, "entry.2060720157" : period_time,
        "entry.920292235" : period_name}




response = urllib.parse.urlencode(data)         #For encoding the data

user_response = url + response                  #Whole URl is concatenated.
try :
        request = urllib.request.urlopen(user_response)
        print(request.getcode())

except:
        print("Error")