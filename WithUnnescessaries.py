Made By HarveyGW
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Imports
import random; import string; from colorama import Fore; import urllib.request
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Random Extension (Single)
def randomExtensionSingle():
    stringLength = int(input(Fore.LIGHTCYAN_EX + "Enter the length of the string: "))
    letters = string.ascii_letters
    rString = (random.choice(letters) for i in range(stringLength))
    String = str(rString)
    print(Fore.YELLOW + "Enter the URL (template says https://[URL NAME]/[EXTENSION]"+'\n'+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    webUrl = input("URL NAME: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Random String is"+" { " + String +" }")
    url = ("https://"+webUrl+"/ " + String)
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
            print("Error Code: "+ e.code)
            print(e.read)
            print()
        main()
    else:
        main()       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Random Extension (looped)
def randomExtensionLooped():
    def randomString(stringLength=int(input(Fore.LIGHTCYAN_EX + "Enter the length of the string: "))):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))
    print(Fore.LIGHTYELLOW_EX + "Enter the URL (template says https://[URL NAME]/[EXTENSION]"+'\n'+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    webUrl = input("URL NAME: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(1, int(input("Enter the amount of times to loop: "))):
        print("Random String is"+" {", randomString()+" }")
        rString = randomString.strip()
        url = ("https://"+webUrl+"/ %s"%rString())
        print("This is the new URL: "+url)
        print(urllib.request.urlopen(url))
        print()
    main()
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
    Choice = input(Fore.LIGHTRED_EX + "Press the corresponding number:"+'\n'+"------------------------------------------"+'\n'+"1.Adds Random Extension (Single)"+'\n'+"2.Adds Random Extension (Looped)"+'\n'+"3.Adds User Inputted Extension (Single)"+'\n'+"4.Adds Extension From File"+'\n'+"------------------------------------------"+'\n')
    if Choice == "1":
        randomExtensionSingle()
    if Choice == "2":
        randomExtensionLooped()
    if Choice == "3":
        setExtensionSingle()
    if Choice == "4":
        readFromFile()
main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

