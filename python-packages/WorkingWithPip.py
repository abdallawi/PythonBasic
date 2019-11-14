import subprocess

# Makes sense:

pip3 = 'pip3'
requests = 'requests'

command_install = 'install'
command_list = 'list'
command_pp = '--format=columns'
command_uninstall = 'uninstall'

# If we want to work with packages from pypi, we can use our package manager pip3.

# We can do allot of things using our package manager:

# 1. Install packages
# 2. Remove packages
# 3. Update packages
# 4. List installed packages
# ...

# Normally we would do these commands from the terminal,
# but because we learned how to run commands from a Python program let's put these lessons to good use:

# Lets install a package using pip3:

subprocess.run([pip3, command_install, requests])

# We can list our installed packages:

print()
subprocess.run([pip3, command_list, command_pp])  # last string is a flag this is optional, makes a prettier printout.

# TL;DR
# In the printout you can see our request package is using a Semantic versioning: 2.21.0 in my case:

# First number stands for:
# MAJOR version when you make incompatible API changes

# Second number stands for:
# MINOR version when you add functionality in a backwards-compatible manner

# Third number stands for:
# PATCH version when you make backwards-compatible bug fixes

# We already installed the latest package from requests, but what if that version is bugged.
# Or it won't work together with your other dependencies[incompatible], you can install a specific version like so:

print()
subprocess.run([pip3, command_uninstall, requests])  # This needs to happen in order to remove previous install!
subprocess.run([pip3, command_install, 'requests==2.9.0'])  # ==<major.minor.patch>

# Lets see in the printout of our installed modules if we have our specific version:
subprocess.run([pip3, command_list, command_pp])

# If we are interested in the patch fixes of a certain minor version of our module,
# we can use a wildcard like so:

print()
subprocess.run([pip3, command_uninstall, requests])
subprocess.run([pip3, command_install, 'requests==2.20.*'])  # ==<major.minor.highest_patch_available>

# Lets see in the printout the specific patch version chosen:
subprocess.run([pip3, command_list, command_pp])

# You can also use the wildcard for the highest compatible minor version:

subprocess.run([pip3, command_uninstall, requests])
subprocess.run([pip3, command_install, 'requests==2.*'])  # This will give you the highest compatible minor version ;)
