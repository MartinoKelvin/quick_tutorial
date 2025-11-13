from setuptools import setup

# List of dependencies installed via `pip install -e .`
requires = [
    'pyramid',
    'pyramid_chameleon',  # masih boleh ada, nggak mengganggu
    'pyramid_jinja2',
    'waitress',
]

# List of dependencies installed via `pip install -e ".[dev]"`
dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
