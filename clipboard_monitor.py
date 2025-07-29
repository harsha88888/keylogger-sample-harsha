import win32clipboard

def get_clipboard_data():
    win32clipboard.OpenClipboard()
    data = ''
    try:
        data = win32clipboard.GetClipboardData()
    except:
        data = ''
    win32clipboard.CloseClipboard()
    return data
