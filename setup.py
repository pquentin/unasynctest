import setuptools

import unasync

setuptools.setup(
    name="unasynctest",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A package used to test unasync",
    packages=['unasynctest', 'unasynctest._async'],
    cmdclass={'build_py': unasync.build_py},
    package_dir={'': 'src'},
)
