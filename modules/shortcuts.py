from win10toast import ToastNotifier


def real_int(number: float):
    return int(round(number, 0))


def alert(title, message, duration):
    toast = ToastNotifier()
    toast.show_toast(
        title=title,
        msg=message,
        icon_path='assets\\icon.ico',
        duration=duration,
        threaded=True   # set threaded=False if you have AttributeError. Idk why it happen sometimes
    )



