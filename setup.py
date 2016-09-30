from setuptools import setup, find_packages
setup(
    name = "glucose-meter",
    version = "0.0.1.dev",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    package_data = {'': ['*.txt', '*.rst', '*.markdown']},
    # metadata for upload to PyPI
    author = "Me",
    author_email = "me@example.com",
    description = "This is an Example Package",
    license = "PSF",
    keywords = "hello world example examples",
    url = "http://example.com/HelloWorld/",
    
    entry_points = { 
                    'console_scripts': [
                                        'test = reader.test:run',
                                        'scan = reader.scan:run'],},
    requires = ['pyserial'],
)