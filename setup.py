from setuptools import setup, find_packages

setup(
    name='Emotion-Recognition',
    version='1.0.0',
    url='https://github.com/brandonkeung/Emotion-Recognition',
    author='Brandon Keung',
    author_email='brandonlkeung@gmail.com',
    description='',
    packages=find_packages(),    
    install_requires=[
        'Pillow',
        'numpy',
        'pandas',
        'tqdm',
        'scikit-learn',
    ],
)