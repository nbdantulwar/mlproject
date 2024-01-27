from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(filepath:str)->List[str]:
    req=[]
    with open(filepath, 'r') as fileobj:
        req=fileobj.readlines()
        print(req)
        req=[re.replace('\n','') for re in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
        print(req)
    return req

setup(
    name='mlproject',
    version='0.0.1',
    author='Nitin',
    author_email='nitin.star123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
