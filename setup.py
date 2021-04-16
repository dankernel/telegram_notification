import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

print(long_description)

setuptools.setup(
    name="telegram_notification", # Replace with your own username
    version="0.0.1",
    author="dankernel",
    author_email="dkdkernel@gmail.com",
    description="A small example package",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/dankernel/telegram_notification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
