from setuptools import setup, find_packages

setup(
   name='passwordgenerator',
   version='1.0',
   description='Provides a simple password generator',
   license='MIT',
   author='Ivan Pomogaev',
   author_email='iwanpomogaev@yandex.ru',
   url='https://github.com/wotiwan/passwordgenerator',
   packages=find_packages(),
   install_requires=['pytest'],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)