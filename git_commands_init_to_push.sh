#Commands used to setup repository and push files

read -p "What is the repository name? " name
read -p "What is the remote url? " url
read -p "Git name? "

#Init commands
echo $name >> README.md
git init
#Add the files on next change
git add *
#Remove a single file
git remove git_commands_init_to_push.sh 
#Tell who you are
git config --global user.name "$name"
#Commit comment
git commit -m "first commit"
#Set branch
git branch -M main
#Set remote url
git remote add origin $url
#send files
git push -u origin main
