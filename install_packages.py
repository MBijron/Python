from install_package import install

# noinspection SpellCheckingInspection
required_packages = [
    "pypiwin32",
    "win32gui",
    "svn"
]

for required_package in required_packages:
    install(required_package)
