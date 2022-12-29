from setuptools import setup, find_namespace_packages


setup(name = 'Clean folder Oleg Veisa',
      version = '0.0.2',
      description = 'Script for sorting files and clear folder',
      url = 'https://github.com/olegveisa/HW7',
      author = 'Oleg Veisa',
      author_email = 'oleg.veisa@gmail.com',
      license = 'MIT',
      classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent'
      ],     
      packages = find_namespace_packages(),
      entry_points = {'console_scripts': [
            'clean-folder=clean_folder_olegveisa.clean:main'
            ]}
)