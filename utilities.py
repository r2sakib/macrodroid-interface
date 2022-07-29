import webbrowser
from winotify import Notification
import pyperclip
import re

def show_notification(title, text):

    toast = Notification(app_id='MacroDroid Interface',
                        title=title,
                        msg=text,
                        icon=r'C:\Users\sakib\OneDrive\codes\macrodroid-interface\icon.png',
                        duration='short')

    toast.show()


def is_url(text: str):
    return bool(re.match(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', text)) 


def action(data: dict):
    show_notification(f"Copied from Phone", data['content'])

    if is_url(data['content']):
        webbrowser.open(url=data['content'], new=0)
    
    print(f"[{data['from']}] Copy: {data['content']}")

