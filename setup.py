from distutils.core import setup

setup(
    name='MEMORY_REDUCER',
    packages=['MEMORY_REDUCER'],
    version='0.1',
    license='MIT',
    description='Python Package to reduce the size and memory of dataframe',
    author='SARAVANAN SAMINATHAN',
    author_email='saravanansaminathan97@gmail.com',
    url='https://github.com/saravanansaminathan/memory_reducer',
    download_url='https://github.com/saravanansaminathan/memory_reducer/archive/master.zip',
    keywords=['MEMORY', 'SIZE', 'REDUCE', 'DATAFRAME'],
    install_requires=[
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
