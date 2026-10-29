# Image named by the local official task-page snapshot.
# Verify availability, tool versions, and digest before pinning the final build.
ARG CONTEST_IMAGE=zhouzhouyi/os-contest:20260510
FROM ${CONTEST_IMAGE}

WORKDIR /workspace
CMD ["/bin/bash"]
