import urllib.parse
import urllib.request
import datetime

url = "https://docs.google.com/forms/d/e/1FAIpQLScf-ISET-XOiEBDyRtpuWIz4S98iC6Nzq247OgIAo4Dvs6vlA/" + "formResponse?&"

email = "santradibbo@gmail.com"
name = "Deeptendu Santra"
section = "A"
roll = "9"
date = datetime.date.today().isoformat()
weekday = datetime.datetime.today().weekday()
period = int(input("Enter the preiod of the day"))

period_to_time = ["1st (9.30am - 10.20am)", "2nd (10.30am - 11.20am)",
                  "3rd (11.30am - 12.20pm)","4th (1.10pm - 2.00pm)",
                  "5th (2.10pm - 3.00pm)","6th (3.10pm - 4.00pm)"]


data = {"entry.375405198":name, "entry.1748177020" : section, 
        "emailAddress" : email, "entry.1479767868" : roll,
        "entry.1691501242" : date, "entry.2060720157" : period_to_time[period-1]}


response = urllib.parse.urlencode(data)

user_response = url + response

request = urllib.request.urlopen(user_response)

print(request.getcode())