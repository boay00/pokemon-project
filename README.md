# Repository for ongoing Pokemon Projects for Data Placement

### Introduction

Overview of Data Science Process, introduction to machine learning concepts.
- Data Loading
- Data Cleaning
- Introduction to Preprocessing
- Introduction to Machine Learning (Linear Regression, Binary Classification, Multi Class Classification)

### Venv Setup and Usage

- Creation of environments

```bash
python3.11 -m venv venv_name
```

- How to activate environment

powershell:

```powershell
.venv_name\Scripts\Activate.ps1
```

bash:

```bash
source venv_name/bin/activate
```

you should see (venv_name) before your terminal line

- Installing requirements

```bash
pip install -r --no-cache-dir requirements.txt
```

- Deactivating venv

bash & powershell:

```bash
deactivate
```

- .gitignore explained

### Linear Regression

- Trained a simple LR model that can predict the speed stat of a pokemon given the rest of the base stats
- Introduced Standard Scaling
- Dataset splitting
  - Train/test
- Fitting the LR model on the training split, evaluating on the test set
  - Introduced concept of overfitting (learning the mark scheme)
- Showcases saving and loading models using the pickle package

### Linear Regression - Extension

Here's a checklist of some things to try and do whilst I'm on AL :)

1. In a single python function named main(), take a pokemon from the database and assign it a new speed stat using your Linear Regression model
   - import packages needed
   - def main()
   - main should:
     - load the pokemon data
     - load the models (scaler and LR model)
     - convert the data to the required format (pandas dataframe)
     - preprocess the data (scale)
       - <i>convert back to dataframe</i>
     - gather prediction from the model
     - (optional) print the output stats using f-strings :)
     - update the pokemons stats in the dictionary
     - save the new updated dictionary to the database
   - This file should be run in the terminal:
  
```bash
python file_name.py
```

Try and get this single command to result in a pokemons stats being generated :)

1. Try and make the script update all pokemon without speed stats, but ignore pokemon with already assigned speed
    - make a new folder perhaps that has all the pokemon without speed stats, and then save them in a new folder which is a complete set? thats up to you, see what you thinks best :)
    - or you could write some code to check if there is an existing "speed" key in the dictionary

### Neural Networks Introduction

- This is the model we will look at developing in order to predict all the stats of a single pokemon
- Not expecting you to work all this out on your own, but if youd like to have a read or watch some youtube videos, you could try these!

Patrick Loeber is very good! Ive not watched this course but this could be a good start :)

#### Part 1: Installation 
https://www.youtube.com/watch?v=hvgnX1gbsLA&list=PLqnslRFeH2Uqfv1Vz3DqeQfy0w20ldbaV&ab_channel=PatrickLoeber

(we should be all good with this one) but in case youre having issues in later videos and imports

#### Part 2: Tensor Basics
https://www.youtube.com/watch?v=PcstG8qiObc&list=PLqnslRFeH2Uqfv1Vz3DqeQfy0w20ldbaV&index=2&ab_channel=PatrickLoeber

#### Part 3: First Neural Network
https://www.youtube.com/watch?v=Edhv7-4t0lc&list=PLqnslRFeH2Uqfv1Vz3DqeQfy0w20ldbaV&index=3&ab_channel=PatrickLoeber

---

I will watch these when i get back and make sure they are useful!!!