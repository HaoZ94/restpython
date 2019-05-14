from distutils.core import setup

setup(
  name = 'restpython',         # How you named your package folder (MyLib)
  packages = ['restpython'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python Implementation of Reference Electrode Standardization Technique',   # Give a short description about your library
  author = 'Hao Zhu',                   # Type in your name
  author_email = 'hz808@nyu.edu',      # Type in your E-Mail
  url = 'https://github.com/Haophdmd/restpython',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Haophdmd/restpython/archive/1.0.0.tar.gz',    # I explain this later on
  keywords = ['EEG', 'REST', 'RE-REFERENCE','PYTHON','TOOLBAOX'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'mne',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
 