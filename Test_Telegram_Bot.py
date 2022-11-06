from requests import post, get
import requests
Token = input("Enter Your Bot Token: ")
Id = input("Enter Your Telegram Id: ")

try :
    post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=New Acount For You :
< Secure >
*••••••••••••••••••••••••••••••••••••••*
Phone Number :- +91808404xxxx
PassWord :- *****
Date :- 6/11/2022
*••••••••••••••••••••••••••••••••••••••*
From :- Saurabh Mishra''')
    print("\n\tSuccessfully massage sent")

except :
    print("\n\tError Occurred")