import os
import yaml

with open(r"C:\Users\Gichimu\Desktop\moringa\dsc-env-config\win_environment.yml") as file_handle:
    environment_data = yaml.load(file_handle, Loader=yaml.Loader)

for dependency in environment_data["dependencies"]:
    # Try splitting by "=" first, then by "=="
    package_info = dependency.split("=", 1)
    if len(package_info) == 1:
        package_info = dependency.split("==", 1)
    
    if len(package_info) == 2:
        package_name, package_version = package_info
    else:
        # Handle the case where there's no version specified
        package_name = package_info[0]
        package_version = None  # You can set a default value or handle this case as needed
    print(f"{package_name} {package_version}")
