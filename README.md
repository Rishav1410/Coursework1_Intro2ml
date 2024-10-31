# Coursework1_Intro2ml

#### Hi all ! This repository contains the source code, outputs and visualizations of Coursework-1 on Decision Trees (70050), October 2024. 
#### This work has been collaborated by Rishav Ghosh (rg1624), Gursimran Saini (gks24) and Edward Wu (eww24). The main code is available at the `Coursework1.ipynb` notebook under `src` folder.

##  Run the code in your local system 
#### To run the code in your local system, you can install the packages in the given `requirements.txt` using `pip`
```bash
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
```

####  Additionally you can also create your own local environment using the following command if you are linux user:
``` bash
    $  python3 -m venv intro2ml
    $  source intro2ml/bin/activate
```
#### For Windows user use `.\scripts\activate` to activate the current virtual environment. Post that install the necessary packages as stated above and you are good to go!
#### Please ensure you name the environment as `intro2ml`. We don't want to track the local dependencies, hence this environment has been added to the `.gitignore`. 
#### For any other names make sure to add your virtual environment to the `.gitignore` !

## Run the code on an Imperial DoC System
#### Running a code any of the Imperial DoC Lab machine is simple, thanks to their already pre-existing `intro2ml` python virtual environment.
#### Just take a clone of this repository 
```bash
    $ git clone https://github.com/Rishav1410/Coursework1_Intro2ml.git
    $ cd Coursework1_Intro2ml
```
#### Once done, you need to activate the virtual environment (the following is from the Coursework Guidelines for this course)
```bash
    $ source /vol/lab/ml/intro2ml/bin/activate
(intro2ml) $ python3 -c "import numpy as np; import torch; print(np); print(torch)"
```
#### You should be able to see the modules are installed. That's it ! You are all set ! Now just navigate to `Coursework1.ipynb` notebook under `src` to get the source code.

## Run the in one of the DoC System through port forwarding
#### This is the final that one can choose, if someone wants a remote server for the development in the backend, while executing in their local system, we have a way for that too!
#### For this scenario we will be using `SSH Tunnelling` to connect to a remote DoC system, start executing Jupyter server in the machine and use port forwarding see the same.
#### This could have been cumbersome everytime trying to execute lengthy `SSH` requests (with multiple hops, by first connecting to a shell server and then to a machine and continue with the rest of the process)
#### A powershell script called `Setup.ps1` has been designed solely for this purpose and makes our life easier. Just type the following if you are in windows command prompt.
``` powershell ./Setup.ps1 -user <IMPERIAL_USER_NAME> ``` 

#### Ensure that you are in the home directory of the repository. Also ensure a clone of the same in the home directory in your DoC systems. 
#### Optionally you can pass an argument `-port <DESIRED_PORT_NUMBER>` to forward it to a particular port in local. By default it will route to `http://localhost:14000/`
#### The above script also utilizes the `sshtolab` script which has been designed by Imperial for remote port forwarding.  
