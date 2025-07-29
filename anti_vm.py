import os

def is_running_in_vm():
    indicators = ['VBOX', 'VirtualBox', 'VMware', 'Xen']
    try:
        with open("/sys/class/dmi/id/product_name") as f:
            name = f.read()
            return any(indicator in name for indicator in indicators)
    except:
        return False
