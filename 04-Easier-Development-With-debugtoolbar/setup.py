from setuptools import setup

# Dependencies wajib
requires = [
    'pyramid',
    'waitress',
]

# Dependencies opsional untuk development
dev_requires = [
    'pyramid_debugtoolbar',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,  # pip install -e ".[dev]"
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main',
        ],
    },
)
