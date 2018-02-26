DOCKER_INSTANCE_NAME := dts_server
DOCKER_IMAGE_TAG := dts_server


serve.dev:
	FLASK_APP=dts_sever FLASK_DEBUG=1 flask run -p 1234

docker.build:
	docker build -t $(DOCKER_IMAGE_TAG) .

docker.run:
	docker run --rm -dit --name $(DOCKER_INSTANCE_NAME) -v beasley_server:/var/lib/weewx $(DOCKER_IMAGE_TAG)
