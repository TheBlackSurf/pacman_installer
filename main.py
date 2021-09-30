import os
import sys




print("""
$$$$$$$\                                                                  
$$  __$$\                                                                 
$$ |  $$ |$$$$$$\   $$$$$$$\ $$$$$$\$$$$\   $$$$$$\  $$$$$$$\             
$$$$$$$  |\____$$\ $$  _____|$$  _$$  _$$\  \____$$\ $$  __$$\            
$$  ____/ $$$$$$$ |$$ /      $$ / $$ / $$ | $$$$$$$ |$$ |  $$ |           
$$ |     $$  __$$ |$$ |      $$ | $$ | $$ |$$  __$$ |$$ |  $$ |           
$$ |     \$$$$$$$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |           
\__|      \_______| \_______|\__| \__| \__| \_______|\__|  \__|           
                                                                          
                                                                                                                                            
 $$$$$$\                                $$\                               
$$  __$$\                               \__|                              
$$ /  \__| $$$$$$\   $$$$$$\ $$\    $$\ $$\  $$$$$$$\  $$$$$$\   $$$$$$$\ 
\$$$$$$\  $$  __$$\ $$  __$$\\$$\  $$  |$$ |$$  _____|$$  __$$\ $$  _____|
 \____$$\ $$$$$$$$ |$$ |  \__|\$$\$$  / $$ |$$ /      $$$$$$$$ |\$$$$$$\  
$$\   $$ |$$   ____|$$ |       \$$$  /  $$ |$$ |      $$   ____| \____$$\ 
\$$$$$$  |\$$$$$$$\ $$ |        \$  /   $$ |\$$$$$$$\ \$$$$$$$\ $$$$$$$  |
 \______/  \_______|\__|         \_/    \__| \_______| \_______|\_______/ 
                                                          
                                                          by MR.DOCTOR                                                                                                                                                                                                                                                                                                       
""")


euid = os.geteuid()
if euid != 0:
    print("Script not started as root. Running sudo..")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print('Running. Your euid is', euid)


def pacman():

    def Install():
        install = input('What you want to install? \nType: ')
        os.system('pacman -S ' + install)
        os.system(install)
        print('')
        cont1 = input('Install again = [1]  Back to menu [2] Exit [99] \nType: ')
        if cont1 == '1':
            Install()
        elif cont1 == '2':
            pacman()
        elif cont1 == '99':
            exit()
        else:
            print('')
            print("[OK, LETS GO TO MENU!]")
            pacman()

    def Update():
        print('UPGRADE MENU')
        os.system('pacman -Syu')
        print('')
        cont2 = input('Update again = [1]  Back to menu [2] Exit [99] \nType: ')
        if cont2 == '1':
            Update()
        elif cont2 == '2':
            pacman()
        elif cont2 == '99':
            exit()
        else:
            print('')
            print("[OK, LETS GO TO MENU!]")
            pacman()

    def Remove():
        remove = input('What you want to remove? \nType: ')
        os.system('pacman -Rs ' + remove)

        os.system(remove)
        print('')
        cont3 = input('Remove again = [1]  Back to menu [2] Exit [99] \nType: ')
        if cont3 == '1':
            Remove()
        elif cont3 == '2':
            pacman()
        elif cont3 == '99':
            exit()
        else:
            print('')
            print("[OK, LETS GO TO MENU!]")
            pacman()

    def Search():
        search = str(input('What you want to search? \nType: '))
        os.system('pacman -Ss ' + search)
        print('')
        cont4 = input('Search again = [1]  Back to menu [2] Exit [99] \nType: ')
        if cont4 == '1':
            Search()
        elif cont4 == '2':
            pacman()
        elif cont4 == '99':
            exit()
        else:
            print('')
            print("[OK, LETS GO TO MENU!]")
            pacman()

    print("""
Welcome to Pacman installer for beginners.

[1] = Install Packman
[2] = Update Packman 
[3] = Remove Packman 
[4] = Search Packman 
[5] = Table install Linux's
    """)
    whatdo = input('[1],[2],[3],[4]: ')
    print('\n')

    if whatdo == '1':
        Install()

    if whatdo == '2':
        Update()

    if whatdo == '3':
        Remove()

    if whatdo == '4':
        Search()
    if whatdo == '5':
        print(""" 
+-----------------------+-------------+----------------+-------------------------+----------------+-----------------+
|        Action         |    Arch     | Red Hat/Fedora |      Debian/Ubuntu      | SLES/openSUSE  |     Gentoo      |
+-----------------------+-------------+----------------+-------------------------+----------------+-----------------+
| Install a package(s)  | pacman -S   | dnf install    | apt install             | zypper install | emerge [-a]     |
| Remove a package(s)   | pacman -Rs  | dnf remove     | apt remove              | zypper remove  | emerge -C       |
| Search for package(s) | pacman -Ss  | dnf search     | apt search              | zypper search  | emerge -S       |
| Upgrade Packages      | pacman -Syu | dnf upgrade    | apt update; apt upgrade | zypper update  | emerge -u world |
+-----------------------+-------------+----------------+-------------------------+----------------+-----------------+

        """)
        cont5 = input('Back to menu [1] | Exit [99] \nType: ')
        if cont5 == '1':
            pacman()
        elif cont5 == '99':
            exit()
        else:
            print('')
            print("[OK, LETS GO TO MENU!]")
            pacman()


pacman()
