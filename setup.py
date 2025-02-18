from setuptools import setup, find_packages

setup(
    name='chanel_project',
    version='0.1.0',
    description='Chanel project for EDHEC Business Data Management',
    packages=find_packages(),
    install_requires=[
        # Add dependencies from requirements.txt automatically
        line.strip() for line in open('requirements.txt') if line.strip() and not line.startswith('#')
    ],
    python_requires='>=3.8',
)
