# Docker Example

This example shows the use of dockerfiles to create different images and in the end make use of them in a DockerCompose.

## Usage

The following command must be run to build the image. The image will have a nginx that will run a static web page. 

```shell
docker build -t nginxserver .
```

Then the same command must be executed with the python application and the reverse proxy 

```shell
docker build -t pythonflask .
docker build -t nginxproxy .

```

Finally, docker compose must be run with the following command:

```shell
docker-compose up -d
```

## Architectures


## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/repository/contributors) who 
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* People you want to thank
* If you took a bunch of code from somewhere list it here
