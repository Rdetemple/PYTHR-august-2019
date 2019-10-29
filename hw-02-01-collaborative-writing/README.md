# Assignment: Collaborative Writing

Today you are going to write a novel but unfortunately, because of time constraints, you’ll need to enlist the help of your friends. You are going to work with others in the class.

The person with the most letters in his or her name is going to be the team leader. This person will *fork* this repository to his or her own account and add the rest of the group as collaborators. Then the rest of the group is going to *clone* this new repository and one by one each of you will write the next sentence. In the end you will have a story that starts off with the sentence we give you and finishes with what you and your group writes.

This assignment is going to teach you how to collaborate on GitHub. This means cloning a repository, pulling the changes that other people have made, and pushing your changes up. You might even come across merge conflicts.

Have fun and don't forget to work alongside a group!

## Learning Goals

* forking Github repos
* adding collaborators to a Github repo
* navigating the command line: `cd`, `ls`
* `git clone`
* `git add`
* `git commit`
* `git push`
* `git pull`
* `git status`

## Assignment

1. The team leader *forks* the [assignment repository](https://git.generalassemb.ly/PYTHR-august-2019/hw-01-01-collaborative-writing). [[How to fork on Github](https://help.github.com/articles/fork-a-repo)]
1. After the repo has been forked, the team leader adds the rest of the group as collaborators. [[How do I add a collaborator?](https://help.github.com/articles/how-do-i-add-a-collaborator)]
1. The rest of the group *clones* the first person's repository.
1. One person pulls the most recent changes, edits the text file, writes the next sentence, makes a commit, and pushes the changes up.
1. Repeat Step 4 until everybody has had a crack at writing the next line in the story.
1. Everybody should take turns writing another line in the story.
1. Once the story is complete, somebody else should take the turn at being the leader, and the team should repeat the entire assignment. You'll have to remove the old assignment repo from your computer, or clone the new story somewhere else, as the name of the repo will be the same every time you repeat.
1. Once every team member has taken a turn at being the leader, submit the assignment!

## Submitting

To submit this assignment:

1. Go to the [assignment's main repo](https://git.generalassemb.ly/PYTHR-august-2019/hw-02-01-collaborative-writing)
1. Click the **Issues** tab
1. Click the **New Issue** button
1. In the Title field, write your name and the title to your story
1. In the comment field, copy and paste the URL to *your* assignment repo
1. Click **Submit new issue** and you're done!

## Important Git Commands

### Git Workflow (Local)

```bash
# creates new git repository on your computer
$ git init

# stages changes to files
$ git add .

# stages changes to all files (including deleted files)
$ git add --all

# shows status of files
$ git status

# creates a new commit (a snapshot in time) with associated message
$ git commit -m "<message>"

# shows history of commits
$ git log
```

### Remote Repositories (Github)

```bash
# sets up the server URL
$ git remote add origin <server url>

# pulls changes on the remote repo to your local repo
$ git pull

# pushes local repo to remote repo
$ git push origin master

# copies a remote repo to your computer
$ git clone <server url>
```

## Additional Resources

* [Collaborating at GitHub Help](https://help.github.com/categories/63/articles)
* [Team Collaboration with GitHub at Tuts+](http://net.tutsplus.com/articles/general/team-collaboration-with-github/)
