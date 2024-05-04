from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT_E = '-e .'

def get_requirements(path:str)->List[str]:
    '''
    This function will return all the requirements.
    '''

    with open(path) as f:
        requirements = f.readlines()
        requirements = [requirement.replace('\n','') for requirement in requirements ]
    
    if HYPHEN_DOT_E in requirements:
        requirements.remove(HYPHEN_DOT_E)
    
    return requirements


setup(
    name='credit_card_fraud_detection_project',
    version='0.0.1',
    author='joocahyadi',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)