from setuptools import setup
from typing import List


def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirements 
    mentioned in requirement.txt file

    return this function is going to return a list which contain name 
    of libraries mentioned in requirement.txt file 
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_file.readlines() 


#Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Gopi"
DESCRIPTION = "This is housing price prediction using machine learning model"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"


setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = PACKAGES,
    install_requires = get_requirements_list()


)