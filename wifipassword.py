# NABEGHEHA.COM

# Github       : https://github.com/NABEGHEHACOM
# Youtube      : https://youtu.be/kc2shu5COos
# Social Media : https://nabegheha.com/socials


# Import subprocess so we can use system commands
import subprocess
# Import the re module so that we can make use of regular expressions.
import re

netsh_output = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", netsh_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:

        wifi_profile = {}

        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(
                ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            password = re.search(
                "Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]

            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])
