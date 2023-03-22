from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='liminal',
      version="0.0.1",
      description="Project_Liminal_MODEL_API",
      license="MIT",
      author="liminal",
      url="https://github.com/LimesAndCrimes/project_liminal",
      install_requires=requirements,
      packages=find_packages()
      )
