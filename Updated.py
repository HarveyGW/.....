
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
  NewUrls = []
  print(Fore.LIGHTYELLOW_EX + "Enter the URL (template says https://[URL NAME]/[EXTENSION]"+'\n'+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  webUrl = input("URL NAME: ")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  with open('Extensions.txt', 'r') as f:
      for line in f:
          if 'str' in line:
              break
          print(line)
          url = ("https://"+webUrl+"/"+line)
          print(Fore.LIGHTYELLOW_EX + "https://"+webUrl+"/"+line)
          try:
              urllib.request.urlopen(url)
              print(Fore.LIGHTGREEN_EX + "Found a good one: " + url)
              NewUrls.insert(1,url)
              with open('file.txt', mode='wt', encoding='utf-8') as myfile:
                for lines in NewUrls:
                  print(lines, file = myfile)
              myfile.close
          except urllib.error.HTTPError as e:
              print(Fore.LIGHTRED_EX + "Error Code: %s" % e.code)
              print(e.read)
              print()
  print("Added to the file")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def main():
    Choice = input(Fore.LIGHTRED_EX + "Press the corresponding number:"+'\n'+"------------------------------------------"+'\n'+"1.Set Extension (Single)"+'\n'+"2.Read From File (Looped)"+'\n'+"------------------------------------------"+'\n')
    if Choice == "1":
        setExtensionSingle()
    if Choice == "2":
        readFromFile()   
main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

