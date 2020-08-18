import urllib
import urllib.parse
import datetime

url = "https://docs.google.com/forms/d/e/1FAIpQLScf-ISET-XOiEBDyRtpuWIz4S98iC6Nzq247OgIAo4Dvs6vlA/" + "formResponse?&"

email = "santradibbo@gmail.com"
name = "Deeptendu Santra"
section = "A"
roll = "9"
date = datetime.date.today().isoformat()

data1 = {"entry.375405198":name, "entry.1748177020" : section, 
        "emailAddress" : email,
        "entry.1479767868" : roll,
        "entry.1691501242" : date}

data = {"emailAddress" : email,"entry.375405198":name,"entry.1748177020" : section,"entry.1479767868" : roll,"entry.1691501242" : date}

response = urllib.parse.urlencode(data)

form_response = url + response

print(form_response)