import setuptools as st

st.setup(
  name='my-minipack',
  version='1.0.0',
  description='How to create a package in python.',
  author='Ayoub ABOUNAKIF',
)

st.find_packages(
  where='src',
  include=['my_minipack'],
  exclude=['tests'],
)

