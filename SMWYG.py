# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
This tool allows you to perform OSINT and reconnaissance on an organization or an individual. It allows one to search 1.4 Billion clear text credentials which was dumped as part of BreachCompilation leak. This database makes finding passwords faster and easier than ever before.
Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar
'''
import os, sys
import requests
from bs4 import BeautifulSoup

def logo():
	logo = '''
        ___          
    . -^   `--,      
   /# =========`-_   
  /# (--====___====\ 
 /#   .- --.  . --.| 
/##   |  * ) (   * ),		+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|##   \    /\ \   / |		|S|h|o|w|M|e|W|h|a|t|Y|o|u|G|o|t|
|###   ---   \ ---  |		+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|####      ___)    #|			Author: Viral Maniar
|######           ##|			Twitter: @ManiarViral
 \##### ---------- / 			Description: This tool allows you to perform OSINT and reconnaissance on an organization or an individual. It allows one to search 1.4 Billion 
  \####           (  				clear text credentials which was dumped as part of BreachCompilation leak. 		
   `\###          |  						
     \###         |  
      \##        |   
       \###.    .)   
        `======/     
	 ***1.4 Billion Clear Text Credentials***
 '''
	return logo

OPTIONS = '''
1. Enter Domain Name to Search Users
2. Enter Specific Email Address
3. Exit
'''

def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def checkInternetConnection():
		try:
			requests.get('https://www.gotcha.pw/')
		except:
			print('[!] No internet connection...Please connect to the Internet')
		else:
			print('[+] Checking Internet connection...')
			print('[+] Connection Successful <3 <3 <3')
			
def cmdDomainSearch():
	Domain = input('Enter Domain Name:').lower()
	pwnedDomain = "https://gotcha.pw/search/" + Domain

	r = requests.get(pwnedDomain)

	#print (r.content)
	soup = BeautifulSoup(r.content, 'html.parser')

	div = soup.find('div', {"class": "col-md-6 fullheight bottombar centerbar pt-3 mb-lg-2 pb-lg-2"})

	print (div.get_text())

def cmdEmailSearch():
	Email = input('Enter Email Address:').lower()
	pwnedEmail = "https://gotcha.pw/search/" + Email

	r1 = requests.get(pwnedEmail)

	#print (r.content)
	soup = BeautifulSoup(r1.content, 'html.parser')

	div1 = soup.find('div', {"class": "col-md-6 fullheight bottombar centerbar pt-3 mb-lg-2 pb-lg-2"})

	print (div1.get_text())
	
cmds = {
	"1" : cmdDomainSearch,
	"2"	: cmdEmailSearch,
	"3"	: lambda: sys.exit(0)
}

						
def main():
	print (logo())
	checkInternetConnection()
	try:
		while True:
			choice = input("\n%s" % OPTIONS)
			if choice not in cmds:
				print ('[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()
