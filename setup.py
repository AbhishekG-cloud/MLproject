from setuptools import  find_packages,setup
from typing import List
hypen = "-e ."
def get_requiremsnts(file_path:str)->List[str]:
    '''
    this function returns requiremnts
    '''
    req_txt =[]
    with open(file_path) as file_obj:
        req_txt = file_obj.readlines()
        req_txt = [i.replace('\n','') for i in req_txt]
    if hypen in req_txt:
        req_txt.remove(hypen)
    return req_txt


setup(
name= "mlproject" ,
version= "0.0.1",
author='Abhishek',
packages=find_packages(),
install_requires=get_requiremsnts('requirements.txt'),
)