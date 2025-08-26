# Image URL to use all building/pushing image targets
REPOSITORY ?= $(REGISTRY)/eformat/rh-brand-ui
REGISTRY ?= quay.io

IMG := $(REPOSITORY):latest

# Build the podman image
podman-build:
	podman build --net=host --platform linux/amd64 . -t ${IMG} -f Containerfile

# Push the podman image
podman-push: podman-build
	podman push ${IMG}
