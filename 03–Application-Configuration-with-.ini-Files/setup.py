from setuptools import setup

# Dependencies yang dibutuhkan project
requires = [
    'pyramid',
    'waitress',
    # opsional untuk ekosistem paste deploy (biasanya ikut saat install pyramid)
    # 'plaster_pastedeploy',
]

setup(
    name='tutorial',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main',
        ],
    },
)
