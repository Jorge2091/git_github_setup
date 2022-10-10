# Intro to ssh
<img src="./images/img.png" />

## What is ssh
ssh(secure shel) is a network protocol that gives a secure way for 2 computers to communicated with one another. For this explaining, the two connections will be from local host computer and the GitHub server.
## How to setup ssh
<img src="https://1v5ymx3zt3y73fq5gy23rtnc-wpengine.netdna-ssl.com/wp-content/uploads/2021/07/GitBashLogo.jpg"/> The first step is to download git bash. This can be done using the fallowing link https://git-scm.com/downloads and then choosing your operating system.
git bash is a standalone application that works similar to your shell/terminal. 

#### How to find .ssh or create a new folder
1. The location where the .ssh file should be found is usually in /c/Users/`username` where `username` is the name of the user. This can be found in /c/Users.
2. if when typing `cd .ssh` and no directory is found. this is when a new folder can be added using the command line `mkdir .ssh`
3. once inside .ssh folder, running the command line `ssh-keygen -t ed25519 -C "your_email@example.com"` where `your_email@example.com` is the email of your github where you have access to the repository. please note, this is the example code for windows only. if using linux or mac, please click <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent"> here</a> and choose the correct operating system. <br/>This command will generate a new and unique key for you to use as a secure connection.
4. just press `enter` to all options they may ask such as passphrase or directory as it is not important. 
5. once key is generated, entering the command `ls` will show two folder `id_ed25519` as one example. view the second file `id_ed25519.pub` with the command `cat id_ed25519.pub`