# Project Boilerplate

A set of files and instructions to help setting up new projects.
The goal is to stop repeating the same stuff and have the necessary boilerplate files ready when you start a project.

## Contents
* [Getting Started](#getting-started)
*    [Prerequisites](#prerequisites)
*    [Installing](#installing)
* [Contributing](#contributing)
*    [Roadmap](#roadmap)
* [Authors](#authors)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install git before using this.

```
sudo apt install git
```

### Installing

Clone this repository

```
git clone https://github.com/MaxValue/Project-Boilerplate.git
```

Rename the created folder to your intended project name

```
mv Project-Boilerplate MyProject
```

Fill in the `REAL_README.md` file.

```
subl -n REAL_README.md
```

Fill in the `REAL_README.md` file.

```
subl -n REAL_README.md
```

Run the `init_project.sh` script.

```
cd MyProject && sudo ./init_project.sh
```

Start programming!

For Python, you will find useful common structures in `util.py`.

## Contributing

If you wanna help, please make an issue.

### Roadmap
Things I already plan to implement, but didn't have yet:
* improve README. [See here](https://github.com/matiassingers/awesome-readme) and [here](https://guides.github.com/features/wikis/) for good examples.
* template for bash
* template for processing
* git init code
	* actually init the repo
	* "create" repo for all platforms
		* LIST HERE
	* multiple origin setup for git commits
		automate this in a script, see also https://gist.github.com/rvl/c3f156e117e22a25f242 and https://stackoverflow.com/questions/5785549/able-to-push-to-all-git-remotes-with-the-one-command
		`git config --global alias.pushall '!git remote | xargs -L1 git push --all'`
* gitignores
	* python
	* html
	* ruby
	* processing
	* lua
* LICENSE (See [here](https://choosealicense.com/) for a list of them)
	* free for all
	* copyrighted
	* some others
* CONTRIBUTING.md
	[compare to other big projects and write it]
* ISSUETEMPLATE.md
	[compare to other big projects and write it]
* GitHub Webpage Template
	[test it out and find the necessary files. see if other platforms have pages support.]
* Wiki structure
	find wiki systems
	maybe i need to start another project only for that
* instructions on how to ...
*   generate pypi packages
* boilerplate code
	* GUI
	* webservers
	* databases
	* argparse
	* configuration files

## Authors

* **Max Fuxjäger** - *Initial work* - [MaxValue](https://github.com/MaxValue)

### Inspiring Sources
* README template by [PurpleBooth](https://github.com/PurpleBooth/) taken from [here](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
