from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this func will return list of rquiremenst
    '''
    requirements =[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements




setup(
name='mlproject',
version='0.0.1',
author='shivam',
author_email='shivam49026@gmial.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn'],
install_requires=get_requirements('requirements.txt')


)