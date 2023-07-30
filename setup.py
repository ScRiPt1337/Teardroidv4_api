import os
import string
import random
import webbrowser

if os.name == 'nt':
    space = os.path.join(os.path.expanduser("~"),'.detaspace','bin','space.exe')
else:
    space =  os.path.join(os.path.expanduser("~"),'.detaspace','bin','space')
    
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def main():
    if os.path.exists(space):
        if os.path.exists("README.md"):
            os.remove("README.md")
        webbrowser.open("https://deta.space", new=2)
        print("create a account in deta.space")
        print("once's your account is created and you can login to your account")
        print("click on the search bar at the bottom of the screen in deta.space home page")
        print("and then click on the settings button")
        print("and then click on the Generate Token button")
        print("it will generate a new token and copy the token paste it below")
        os.system(space + " login")
        os.system(space + " new -n " + generate_random_string(10))
        os.system(space + " push")
    else:
        print("space is not installed")
        print("installing space cli....")
        if os.name == 'nt':
            os.system("powershell -c \"iwr https://deta.space/assets/space-cli.ps1 -useb | iex\"")
        else:
            os.system("curl -fsSL https://deta.space/assets/space-cli.sh | sh")
        
        print("\nPlease run this script again!")
        
main()
