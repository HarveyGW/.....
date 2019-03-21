Made By HarveyGW
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Imports
from colorama import Fore; import urllib.request
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def setExtensionSingle():
    print(Fore.LIGHTGREEN_EX + "Enter the URL (template says https://[URL NAME]/[EXTENSION]"+'\n'+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    webUrl = input("URL NAME: ")
    Extension = input("EXTENSION: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    url = ("https://"+webUrl+"/"+Extension)
    print("This is the new URL: " + url)
    a = input("Do you want to try and connect to this new URL? (y/n) ")
    if a == "y":
        try:
            print(urllib.request.urlopen(url))
            response = urllib.request.urlopen(url)
            ans = input("Do you want to read the HTML? ")
            if ans == "y":
                print(response.read())
            else:
                main()
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read)
            print()
        main()
    else:
        main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def readFromFile():
    print(Fore.LIGHTRED_EX + "Enter the URL (template says https://[URL NAME]/[EXTENSION]"+'\n'+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    webUrl = input("URL NAME: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('Extensions.txt', 'r') as f:
        for line in f:
            if 'str' in line:
                break
            print(line)
            url = ("https://"+webUrl+"/"+line)
            print("https://"+webUrl+"/"+line)
            try:
                urllib.request.urlopen(url)
            except urllib.error.HTTPError as e:
                print("Error Code: %s" % e.code)
                print(e.read)
                print()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def main():
    Choice = input(Fore.LIGHTRED_EX + "Press the corresponding number:"+'\n'+"------------------------------------------"+'\n'+"1.Set Extension (Single)"+'\n'+"2.Read From File (Looped)"+'\n'+"------------------------------------------"+'\n')
    if Choice == "1":
        setExtensionSingle()
    if Choice == "2":
        readFromFile()   
main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

