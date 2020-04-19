t() {
	cd $PREFIX/bin
	if [ -e toilet ];then
	printf "\n\n\033[92m Toilet is installed !!"
	else
	printf "\n\n\033[92m[×]\033[91m Toilet not installed !!!"
	printf "\n\n\033[92m Installing toilet.....\n"
	apt update
	apt upgrade
	apt install toilet
	printf "\n Seccessfully installed"
	fi
	f
	}
	f() {
		cd $PREFIX/bin
	if [ -e figlet ];then
	printf "\n\n\033[92m figlet is installed !!"
	else
	printf "\n\n\033[92m[×]\033[91m figlet not installed !!!"
	printf "\n\n\033[92m Installing figlet.....\n"
	apt update
	apt upgrade
	apt install figlet
	printf "\n Seccessfully installed"
	fi
	}
	t