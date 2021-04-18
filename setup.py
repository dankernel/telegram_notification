import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telegram_notification", # Replace with your own username
    version="0.1.9",
    author="dankernel",
    author_email="dkdkernel@gmail.com",
    description="Powerful utility to send telegram alarms from cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dankernel/telegram_notification",
    packages=setuptools.find_packages(),
    install_requires = ['python-telegram-bot'],
    scripts=['telegram_notification/noti', 'telegram_notification/config.ini'],
    package_data = {'': ['telegram_notification/config.ini']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
