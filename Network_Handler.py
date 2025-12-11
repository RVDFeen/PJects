#import wmi

#nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

#def change_ip(ip):
    #print(ip)

#change_ip()