The_little_mermaid = 3
Brother_Bear = 5
Hercules = 1
cost = 3
total_days = The_little_mermaid + Brother_Bear + Hercules
total_cost = total_days * cost
print("The total cost for the movies is", total_cost, "dollars")




# Suppose you are working as a contractor for 3 companies: Google, Amazon, Facebook,
# they pay you a different rate per hour. Google pays 400/hr, Amazon 380/hr, and FB 350.
# How much will you recive in pmt this week?  10 hrs FB, 6 hrs GGL, 4 hrs Amazon.

google_hr = 400
google_hrs_worked = 6
google_pay = google_hr * google_hrs_worked

amazon_hr = 380
amazon_hrs_worked = 4
amazon_pay = amazon_hr * amazon_hrs_worked

fb_hr = 350
fb_hrs_worked = 10
fb_pay = fb_hr * fb_hrs_worked

total_pay = google_pay + amazon_pay + fb_pay
print("This week you will recieve", total_pay, "dollars.")



# A student can be enrolled to a class only if the class is not full and the 
#class schedule does not conflict with her current schedule.

class_full = False
schedule_conflict = False
enrollable = not (class_full or schedule_conflict)

enrollable



# A product offer can be applied only if people buys more than 2 items,
# and the offer has not expired.  Premium members do not need to buy a specific amt.

Offer_expired = False
More_than_2_items = True
Premium_members = True

offer_applied = Premium_members or (More_than_2_items and not Offer_expired)

print (offer_applied)


#Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

len(password) >= 5
len(username) <= 20
password != username

#bonus








