from setuptools import setup
import versioneer

requirements = ["rioxarray"]

setup(
    name='shbaam',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Satellite Hydrology Bits Analysis And Mapping",
    license="MIT",
    author="BYU-Hydroinformatics",
    author_email='pulla@byu.edu',
    url='https://github.com/byu-hydroinformatics/shbaam',
    packages=['shbaam'],
    entry_points={
        'console_scripts': [
            'shbaam=shbaam.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='shbaam',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
