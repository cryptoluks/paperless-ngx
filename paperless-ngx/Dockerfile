# Build stage for zxing-cpp
FROM docker.io/library/python:3.11-bookworm as builder

# Install build dependencies
RUN apt-get update && \
    apt-get -y install \
    cmake \
    g++ \
    git \
    unzip \
    wget

# Install zxing-cpp python from repo
RUN wget --progress=bar:force:noscroll https://github.com/zxing-cpp/zxing-cpp/archive/refs/heads/master.zip && \
    unzip master.zip && \
    rm master.zip && \
    cd zxing-cpp-master/wrappers/python && \
    python setup.py install

FROM ghcr.io/paperless-ngx/paperless-ngx

# Copy built files from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages/zxing_cpp*.egg /usr/local/lib/python3.11/site-packages/
