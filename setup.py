from setuptools import setup, find_packages

setup(
    name='ample',
    version='0.1',
    description='Geometry-preserving random sampling',
    url='https://github.com/brianhie/ample',
    download_url='https://github.com/brianhie/ample/archive/v0.1-alpha.tar.gz',
    packages=find_packages(exclude=['bin', 'conf', 'data', 'target', 'R']),
    install_requires=[
        'fbpca>=1.0',
        'numpy>=1.12.0',
        'scikit-learn>=0.20rc1',
    ],
    author='Brian Hie',
    author_email='brianhie@mit.edu',
    license='MIT'
)
