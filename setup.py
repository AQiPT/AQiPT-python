from pathlib import Path
from setuptools import setup, find_packages

setup(
    name = 'AQiPT',
    version = '2.0.0.2',
    author = "Manuel Morgado & S. Whitlock",
    author_email = "manuelmorgadov@gmail.com, whitlock@unistra.fr ",
    description = ("AQiPT: Atomic Quantum information Processing Toolbox"),
    long_description = Path("readme.md").read_text(),
    long_description_content_type = "text/markdown",
    license = "BSD-3",
    url = "https://github.com/AQiPT/AQiPT-python/",
    package_dir = {'':'src'},
    project_urls = {
        "Documentation": "https://github.com/AQiPT/AQiPT-python/tree/main/docs",
        "Source": "https://github.com/AQiPT/AQiPT-python/"
    }
    packages = find_packages(where='src'),
    include_package_data = True,
    classifiers=[
        "Development Status :: 5 - Alpha",
        "Intended Audience :: Developers, Physicists:,
        "Topic :: Quantum Information, OS, Control Systems",
        "License :: OSI Approved :: BSD-3 License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires = "≥3.9",
    install_requires=[
        'numpy',
        'qutip',
        'scipy',
        'networkx',
        'matplotlib',
        'tqdm',
        'qiskit',
        'plotly',
        'pairinteraction'   
    ],
)
