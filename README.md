# postman collection generation

[![PyPI version](https://badge.fury.io/py/postman-collection-generation.svg)](https://badge.fury.io/py/postman-collection-generation)

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

## Installation

You can install the Real Python Feed Reader from [PyPI](https://pypi.org/project/postman_collection_generation/):

    pip install postman_collection_generation

## How to use

You can call the function :

    >>> from postman_collection_generation import generate_collection
    >>> generate_collection(flask_app,name='collection file name',url_domain='localhost',port=5000,output_path = '.')
    

