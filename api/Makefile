# Image URL to use all building/pushing image targets
REPOSITORY ?= $(REGISTRY)/eformat/rh-brand-api
REGISTRY ?= quay.io

IMG := $(REPOSITORY):latest

# Build the podman image
podman-build:
	podman build --platform linux/amd64 . -t ${IMG} -f Containerfile

# Push the podman image
podman-push: podman-build
	podman push ${IMG}
