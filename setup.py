from setuptools import find_packages,setup
from typing import list
HYPEN_E_DOT='-e .'
def get_requirement(file_path:str)->list[str]:
    ...
    # this function will return the list of requirement
    ...
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirements=[req.replace ("\n" ,"") for req in requirement.txt]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT) 
    return requirement

setup (
    name="MLPROJECT", 
    version="0.0.1",
    author="Data Tycoon",
    author_email="healthanalyst7@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')
    
)
