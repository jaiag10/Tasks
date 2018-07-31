import os
import json

dependency_file = 'pipfile.json'
failed = []

def install_pkgs(dependencies):
    failed_pkgs = []
    for pkg in dependencies:
        print("Trying to install " + pkg)
        return_code = os.system('pip install ' + pkg)
        if return_code != 0:
            failed_pkgs.append(pkg)
        else:
            print("Successfully Installed " + pkg)
    return failed_pkgs

with open(dependency_file) as deps_file:
    data = json.load(deps_file)

dependency = data.get('dependecy')
if dependency:
    print("Trying to install dependencies")
    failed += install_pkgs(dependency)

if failed:
    print("Failed to install following packages..")
    for pkg in failed:
        print(pkg)