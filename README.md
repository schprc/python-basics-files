source: [OpenTechShool Berlin](http://opentechschool.github.io/social-coding/)

Setting up
==========

Create a GitHub account
-----------------------

The first and easiest thing to do is setup a GitHub account. Most people use the GitHub Free account, which gives you unlimited public repositories. You can sign up https://github.com/

Note that GitHub is designed around sharing with the whole world. With a free account, everything you upload will be publicly available. This includes the email address that you use when you configure Git.

Download and install Git
------------------------

We’ll be using the plain command-line Git. The easiest way to install Git on Mac or Windows is to use the prepackaged GitHub for Mac and GitHub for Windows. Not only do they provide the Git command line, but they also include a GUI interface to streamline some interactions with GitHub https://mac.github.com/

Your first repository
=====================

terminal commands
-----------------

`cd` change directory (`cd ..` = will go one level up)
`ls` list directory content
`pwd` print working directory
`touch README` it will create file README
`mkdir directoryname` will create directory

git commands
------------

`git init myfirstrepo` will create directory "myfirstrepo"
`git add` add file
`git rm` remove file
`git status` git will let you know the current status of your repository

Add a file
----------

We can put any type of file into Git. It is especially good at keeping track of text files such as Python, Javascript, HTML and CSS. A very common file is the README, which is used to tell people what the repository is about. Create a new file called README inside myfirstrepo/ with your text editor. (You can make it in Sublime and save in the directory, then open it via terminal.)

`git add <file>` will add file with "file" name
`git add .` will adda all file sin directory

```
git commit -m "Initial commit" 
```

(`-m` = short msg)

if you write `git status`, it shows no changes
if you change file and write `git status` it will show changes

And log will tell us that the commit is now in the repository:
`git log`

Git has saved a snapshot of your repository at the moment you committed. If you will take a look at git status it will tell you that your directory is currently ‘clean’, meaning that nothing has changed since the commit. You can always return your directory back to any commit in your history. Likewise, you can also fast-forward your directory to commits in your future, for example when somebody has made a change that you would like to add to your repository. But we’ll get to that later when we discuss pulling changes from others.

Commits are on branches
-----------------------

In the example, you may have noticed the word `master` several times. In Git, commits are organised into `branches`. The branch master is the default branch name for a new Git repository. You can think of branches as timelines of changes.

At the moment, your repository is very simple. There is just a single commit, and the master branch is a label that points to it. Like so:

```bash
o  <-- master
```

Now say you have made some more changes. Like before you’ll use add and commit to create a new commit. Git knows you are on the master branch, so it looks at the commit master points to, adds your commit to it, and points master to your new commit. Now you have two commits in your repository, and the master branch points to the new one.

```bash
o  <-- master
|
o
```

There isn’t anything special about a branch. It is just a label that we add to the latest commit you made. It’s a much easier way than typing out the identifier of the commit, which is a crazy-long unique hash string.

Multiple branches
-----------------

We won’t be getting too deep into this today, but branches become very useful in day-to-day use by teams, as they allow you to experiment with topic branches. It’s like fan-fiction for developers! You can make a branch off the official master branch, then if people like them you can merge the branch back into master. Git is very smart about merging changes, making it very easy to use once you get the hang of it.

It can get very complicated over time, when a project might have at least a dozen active branches at any one time. But Git is very good at managing lots of branches. Even the Git project itself has gotten a little crazy at times with the number of branches!

Pushing to GitHub
-----------------

Now that we have this fantastic local repository, it’s time to change the world by sharing it on GitHub!

Fortunately, the process is pretty simple. We’ll create a repository on GitHub using the exact same name, then push our repository to GitHub. At the end we will have two repositories: the one on your computer, and the one at GitHub.

Create a repository called ‘myfirstrepo’ on the new repository page. Leave all the options as default.

Now, on that web page, see the section Push an existing repository from the command line. It has the two key commands you’ll need, tailored for your repository.

```bash
git remote add 
```
associates your local repository to your GitHub repository, which will be called origin (which is a Git convention for the default remote repository). You could also call it github or upstream or anything you like, as it only applies to your local repository.

```bash
git push 
```
pushes commits to origin (GitHub) from the branch master (the default branch). Then the -u option tells Git that we want to push to a branch called master on the remote repository called origin as the default in future, so we don’t have to type it every time. Our local and remote master branches are now linked.

if you change some file
-----------------------

$ git status (will show you modified file)
$ git commit -am "README update" (or any diffferent cahnge as update, just as a note for yourself)
$ git push origin master (paste it on GitHub account)

Clone files from git to my computer
-----------------------------------

1. Go to a directory
```
cd mydir
```
2. clone a repository
```bash
git clone [here](https://github.com/kr15h/RPi-Setup.git)
```
3. Check if it is cloned by listing current dir
```bash
ls
```
4. It should show that RPi-Setup is there
5. Navigate to that directory
cd RPi-Setup
6. use it - for example check git log
```bash
git log
```
7. It should show the history of the repository

Social Coding in the Underground
================================

Fork this!
----------

Add someone as a collaborator on git
Collaborator downloades clone version of your file
He/she changes something
```bash
git commit -am "description"
```
```bash
git push origin master
```

Markdown
--------

```bash
git mv README README.md
```

alt + ~ = ``

It is a git version of the `mv` command. It renames README to README.md and does everything to keep the git repository in tact (remove README from and add README.md to the repository).

More about GitHub markdown read [here](https://github.com/schprc/python-basics-files.git)

and/or (without spaces):
hash + text (is a large heading),
multiply + text + muliply (text in italic),
multiply multiply + text + muliply multiply (strong text) 



