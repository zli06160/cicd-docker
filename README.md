# CICD-Docker 
A personal practice repo, mainly contains a simple test for the uniswap v2 price calculator.

### Branch Architecture

``master``: protected branch for the PRODUCTION & releases, only the administrator has the right to touch it. 

``develop``: protected branch for integration.

``feature/featureName``: branch for adding new features, should be rebased on develop branch before making pull requests.

``fix/bugName``: branch for bug fixing, should be rebased on master(or develop) branch.


### Release Versioning
Any new changes to master branch have to be validated(reviewed and tested) on the develop branch before being accepted.

A release version, based on a master branch which is fully validated, should be called ``release-YYYYMMDD``, or ``release-YYYYMMDD-V*`` if needed. 

### Coding conventions
[PEP8](https://peps.python.org/pep-0008/)

[Dockerfile](https://docs.docker.com/engine/reference/builder/)



