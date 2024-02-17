#
# help
#
help_docker_base:
	@echo ""
	@echo "-------------------- Docker: Basic commands ----------------------"
	@echo "make build-prod ---------------- Build the prod image"
	@echo "make clean-all ----------------- Delete all images"
	@echo "make clean-prod ---------------- Delete the prod image"
	@echo "make kill-all ------------------ Stop all images"
	@echo "make kill-prod ----------------- Stop the prod image"

build-prod:
	@echo "executing target build-prod"
	@docker build \
		-t ${CONTAINER_IMAGE_NAME_PROD} \
		.

#
# docker maintenance targets
#
clean-all: clean-prod

clean-prod:
	@echo "executing target clean-prod"
	@docker rmi ${CONTAINER_IMAGE_NAME_PROD} --force

kill-all: kill-prod

kill-prod:
	@echo "executing target kill-prod"
	@docker kill ${CONTAINER_IMAGE_NAME_PROD}
