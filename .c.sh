ch() {
	cd $PREFIX/bin
	if [ -e msfconsole ];then
	printf "\n\n\033[93m Successfully installed metasploit\n"
	read
	else
	printf "\n\n\033[91m[×]\033[92 metasploit not installed!!!!"
	fi
	}
	ch
	read