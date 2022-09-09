CommonRoad
------------------------------

This is a meta-package which automatically installs all CommonRoad tools currently released on PyPi.

For more details to the individual tool, please see our [website](https://commonroad.in.tum.de/).


Tools
------------
Currently, the following CommonRoad tools will be installed when downloading this meta-package:

* commonroad-io
* commonroad-drivability-checker
* commonroad-vehicle-models
* commonroad-route-planner
* sumocr


Installation
------------
To automatically install the above mentioned tools, please run:
```
pip install commonroad-all
```


Updating the Meta-Package
-------------------------
The version numbers should always be fixed to avoid incompatibilities when individual packages have been updated. Steps for updating the meta-package:
* update dependencies in `setup.py`: Update list entries in `install_requires`
* update the version number of the meta-package
* build wheel and push to Pypi
