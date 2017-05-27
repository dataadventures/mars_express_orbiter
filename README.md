# Data Science Hackathon - Data Adventures - starter code

This repository is meant to help you start that competition :) 
Feel free to change the code, add new files and fix possible bugs. 
You don't have to use it! However, we believe it may be useful.

Repository content:
* **hackathon** - python module with utils function and a simple parser of the DMOP file. This is a good point to start your project.
* **notebooks** - jupyter notebooks which show how to read data, parse them, create and exemplary dataset and simple model with Keras etc. 
* **data** - a directory for dataset files. 

# Datasets

* Main dataset is located at: ![Download](https://www.kaggle.com/europeanspaceagency/mars-express-power-hackathon)
* FORNAX, augmented dataset (more data) is located at: ![Download](https://www.kaggle.com/fornaxai/dataadventures)

## Where to unpack data?

Unpack the files so that folders *train_set* and *test_set* reside in the **data** directory of the project. 
To use the provided code with the `Main dataset` file names have to be changed so that the prefix is omitted,
eg. change `test_set/context-2015-01-01_2015-07-01--saaf.csv` to `test_set/saaf.csv`. 
Then put the `sample_power--2015-01-01_2015-07-01.csv` into the `test_set` folder and rename the file as `power.csv`.


# How to use the code?

The code is written in python2.7 (however it should also work with >3 versions) and it was tested on Ubuntu 16.04 system. 
We suggest you to install the *anaconda* software which is a simple tool for managing multiple python versions, in case
if you are worrying of possible dependency conflicts. 

When using the anaconda enviroment management you should start from installing some necessary libraries.
Here are the steps:

* Setup a new conda enviroment: `conda create --name hackathon python=2.7`
* Activate the enviroment: `source activate hackathon`
* Install necessary libraries: `conda install pandas numpy tqdm matplotlib`
* For people who want to install tensorflow with GPU support: 
 * Install keras library with pip: `pip install keras` - do not install keras with conda install, it will automatically install tensorflow without GPU support
 * `pip install tensorflow-gpu`
* For those who do not care about GPU support:
 * Install keras with conda: `conda install keras`

# How to make python modules working?

* Run `pip install -e .` in the project root folder. 

With this command you can `import hackathon` module from your python console.
 
# Happy feature engineering!
