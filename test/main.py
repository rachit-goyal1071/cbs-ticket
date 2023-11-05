import taipy as tp
from taipy.gui import Gui
import json

from taipy import Core
from pages import *

import webbrowser


page = """
<|{title1}|text|class_name=title1-css|format=%.9f|>
<|navbar|lov={[("page1", "Home"), ("https://en.wikipedia.org/wiki/Nehru_Planetarium", "About Us")]}|>
<br/>
<|{logo1}|image|label=Kashmir Valley|on_action=image_load|width=430px|height=300px|>
<|{logo2}|image|label=Udaipur Palace|on_action=image_load|width=430px|height=300px|>
<|{logo3}|image|label=Himalayas|on_action=image_load|width=430px|height=300px|>
<br/>
<|{title2}|text|class_name=title2-css|format=%.9f|>
<br/>
No. Of Tickets: <|{tickets_quan}|>
<br/>
<|{tickets_quan}|slider|min=1|max=10|>
<br/>
Name:
<|{input_name}|input|class_name=title-name-css|>
<br/>
Location
<|{location}|input|class_name=title-location-css|>
<br/>
<|{adhaar}|file_selector|label=Uplod Adhaar|on_action=function_name|extensions=.csv,.xlsx|drop_message=Drop Message|class_name=adhaar-btn|>
<br/>
Price: <|{tickets_quan}|>
x 300

<br/>
<|{submit_b}|Submit|button|class_name=submit-btn|>
<br/>

"""
tickets_quan = 1
title1 = "World Lens"   
title2 = "Book Tickets"


logo1 = "assets/logo1.jpg"
logo2 = "assets/logo2.avif"
logo3 = "assets/logo3.jpeg"

def submit_scenario(input_name,location):
    data = {
        "input_name": input_name,
        "location" :location
    }
    with open("taipy.json", "w") as f:
        json.dump(data,f)


def image_load(state):
    webbrowser.open("https://taipy.io")



Gui(page=page).run(dark_mode=True)
