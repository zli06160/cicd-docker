# cicd-docker
A personal practice repo, mainly contains an integration test for the uniswap v2 price calculator.

### How to run the test with Docker
Build docker image:<br/>
```docker build -t <your-image-name> .```

Run the docker image as a container on docker environment:<br/>
```docker run --name <your-container-name> <your-image-name>```


### Branch Architecture

``master``: protected branch for the PRODUCTION & releases, only the administrator has the right to touch it. 

``develop``: protected branch for integration.

``feature/featureName``: branch for adding new features, should be rebased on develop branch before making pull requests.

``fix/bugName``: branch for bug fixing, should be rebased on master(or develop) branch.


### Release Versioning
Any new changes to master branch have to be validated(reviewed and tested) on the develop branch before being accepted.

A release version, based on a master branch which is fully validated, should be called ``cicd-docker:v*.*.*``(e.g.[cicd-docker:v1.0.2](https://hub.docker.com/layers/zli06160/cicd-docker/))


### Coding conventions
[PEP8](https://peps.python.org/pep-0008/)

[Dockerfile](https://docs.docker.com/engine/reference/builder/)



