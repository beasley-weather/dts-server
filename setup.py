from setuptools import setup


setup(
    name='dts-server',
    packages=['dts_server'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pyzmq'
    ]
)
