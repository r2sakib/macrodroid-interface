from winotify import Notification


def show_notification(title, text):

    toast = Notification(app_id='MacroDroid Interface',
                        title=title,
                        msg=text,
                        icon=r'C:\Users\sakib\OneDrive\codes\macrodroid-interface\icon.png',
                        duration='short')

    toast.show()