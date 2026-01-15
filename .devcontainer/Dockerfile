FROM mcr.microsoft.com/devcontainers/python:3.12

WORKDIR /home/vscode
USER vscode

RUN mkdir -p .ssh && chmod 700 .ssh

RUN ssh-keyscan -t ecdsa github.com >> .ssh/known_hosts

RUN sudo apt-get update
RUN sudo apt-get install --no-install-recommends --assume-yes \
    libx11-dev \
    libgl1 \
    libopenmpi-dev \
    libosmesa6-dev \
    x11-apps \
    git-lfs \
    curl

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN git lfs install