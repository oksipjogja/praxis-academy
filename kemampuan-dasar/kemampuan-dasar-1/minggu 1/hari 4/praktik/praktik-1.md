# Create a folder for my project.
mkdir praxis-academy
cd praxis-academy

# To make this directory and empty Git repo do this:
git init 

# I usually create an empty README.txt file for the first commit in my project
# history. 
touch README.txt 
git add README.txt 
git commit -m 'First commit.' 

# Add some explanation about the project to the README file.
echo 'This repo is a collection of my favorite praxis-academy.' >> README.txt

# Review uncommitted changes. Then commit them.
git status
git diff
git add README.txt
git commit -m 'Added project overview to README.txt'

# Donie dowload favorite praxis-academy.
wget https://github.com/praxis-academy/akademik.txt

# The files have been downloaded, but not committed.

# You can see this with git status. git status

# Donie adds the files one-by-one to make her git history look nice and tidy.
git add praxis-academy-akademik.txt 
git status 
git commit -m 'praxis-academy-akademik.txt.'

# Donie reviews and admires her commit history.
git log
git log --oneline
git log -p

# Next, Donie creates a GitHub account here: https://github.com/. Then she creates a new repo named praxis-academy". Following the instructions provided by GitHub,

git remote add origin https://github.com/bryanhirsch/rhymes.git
git push -u origin master
