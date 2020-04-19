import os
import time
print("\033[92m")
print("\033[92m Checking Requirements")
time.sleep(2)
os.system("bash .check.sh")
os.system("clear")
def me():
	os.system("clear")
	os.system("toilet -f mono12 -F metal Thanx")
	print("\033[93m For using this\n\n")


os.system("figlet Metasploit")
print("\n\033[92m[\033[0m1\033[92m]\033[93m 5.0 or 6.0 only")
print("\033[92m[\033[0m2\033[92m]\033[93m 7.0 or ,7.0+ only")
a = input("\n\033[95mMetasploit\033[0m@\033[93mInstall >>  ")
if a == "1":
	print("Installing metasploit")
	os.system("#curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz;gunzip metasploit_5.0.65-1_all.deb.gz;dpkg -i metasploit_5.0.65-1_all.deb;apt -f install")
	os.system("clear")
	print("\nSuccessfully installed metasploit")
	me()

if a == "2":
		print("\n\033[92m Installing metasploit")
		os.system("pkg install unstable-repo")
		os.system("pkg install metasploit")
		os.system("#clear")
		print("\033[93m Successfully installed metasploit")
		me()