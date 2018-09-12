from setuptools import setup
import io, re, os

def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

version = find_version('driveanon', '__init__.py')

setup(
    name='driveanon',
    version=version,
    description='Module for reading Google Drive files anonymously',
    long_description='README.md',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3',
    url='https://github.com/tjcrone/driveanon',
    author='Tim Crone',
    author_email='tjcrone@gmail.com',
    license='MIT',
    packages=['driveanon'])
