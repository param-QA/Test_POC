FROM ubuntu:latest

# Intentional bad practice: running as root
USER root

# Intentional bad practice: no version pinning
RUN apt-get update && apt-get install -y curl

CMD ["bash"]
