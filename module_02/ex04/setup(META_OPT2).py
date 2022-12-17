import setuptools as st

st.setup(
  name='my_minipack',
  version='1.0.0',
  description='How to create a package in python.',
  author='aabounak',
  author_email='aabounak@student.1337.ma',
  license='GPLv3',
  packages=st.find_packages(
    where='src',
    include=['my_minipack'],
    exclude=['tests'],
  ),
  package_dir={'':"src"},
  python_requires='>=3.7',
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Students",
    "Topic :: Education",
    "Topic :: HowTo",
    "Topic :: Package",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only"
  ],
)

