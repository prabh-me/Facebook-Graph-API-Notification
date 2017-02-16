import requests

files = {
    'template': 'SBI PO Recruitment 2017: Exam Dates, Notification, Eligibility Details',
    'ref': '31_day_inactive_LF_8_Feb', # campaign_name
    'access_token': '', # access_token
    'href': '' # Redirect URL
}

requests.post('https://graph.facebook.com/"""+fb_user_id+"""/notifications', files=files)
