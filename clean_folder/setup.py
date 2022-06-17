from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.1',
    description='Homework 7. Clean folder',
    #url='http://github.com/dummy_user/useful',
    author='Andrij Prytulskij',
    author_email='andrij0402@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    #install_requires=['markdown'],
    entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
)