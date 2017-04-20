https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
# A test of syntax highlighting notes

TL;DR

pip and virtualenv are the only things that need to be installed globally (really just virtualenv, contains pip)


# use:
cd ~/code/myproject
virtualenv env # convention to call virtualenv directory containing the environment, 'env'
	# Add env to gitignore
	# Why?
	#http://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository
	# TL;DR use a requirements.txt and load that instead


######## Use conda instead
# http://stackoverflow.com/questions/34398676/does-conda-replace-the-need-for-virtualenv
# https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
# http://tdhopper.com/blog/2015/Nov/24/my-python-environment-workflow-with-conda/
# https://conda.io/docs/using/envs.html

# Create:
	# To see available pythons:
	conda search "^python$"
conda create --name <envname> python=<version> <optional dependencies>
conda create -n yourenvname python=x.x anaconda

# Activate
source activate yourenvname

# Deactivate
source deactivate

# Remove:
conda env remove --name <envname>
