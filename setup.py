from distutils.core import setup

setup(
    name="brightcoveCMS-python",
    version="0.1",
    license="GPL",
    description="a python wrapper from the Brightcove CMS API",
    author="Greg McCoy",
    author_email="gmccoy4242@gmail.com",
    url="https://github.com/gregmccoy/brightcoveCMS-python",
    requires=[
        'requests',
    ],
    packages = ['brightcoveCMS'],
)
