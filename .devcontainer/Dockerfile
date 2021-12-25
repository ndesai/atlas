FROM ubuntu:20.10

RUN apt -y update && \
    apt -y install python3 pip git \
    silversearcher-ag vim

RUN apt -y update && \
    apt -y install clang-11

RUN apt -y update && \
    apt -y install wget libssl-dev

ARG CMAKE_VERSION=3.20.3
RUN wget -q https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz \
    && tar -xzf cmake-${CMAKE_VERSION}.tar.gz \
    && cd cmake-${CMAKE_VERSION} \
    && ./bootstrap -- -DCMAKE_BUILD_TYPE:STRING=Release && make -j1 && make install \
    && cd ../ && rm -rf cmake-${CMAKE_VERSION}*

RUN apt -y update && \
    apt -y install autoconf libtool pkg-config automake curl unzip g++ make

ARG PROTOBUF_VERSION=3.17.1
RUN wget -q https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-cpp-${PROTOBUF_VERSION}.tar.gz \
    && tar -xzf protobuf-cpp-${PROTOBUF_VERSION}.tar.gz \
    && cd protobuf-${PROTOBUF_VERSION} \
    && ./configure && make -j2 && make install

# Golang installation
ARG GOLANG_VERSION=1.16.4
ENV GOARCH=arm64
ENV GOOS=linux
ENV GOBIN=/usr/local/go/bin
RUN wget -q https://golang.org/dl/go${GOLANG_VERSION}.linux-arm64.tar.gz \
    && rm -rf /usr/local/go && tar -C /usr/local -xzf go${GOLANG_VERSION}.linux-arm64.tar.gz

ENV PATH="${PATH}:${GOBIN}"

# Golang protoc
RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@latest \
    && go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

RUN apt -y update && \
    apt -y install libc-ares-dev

ARG GRPC_VERSION=v1.38.0
RUN git clone --depth=1 --branch=${GRPC_VERSION} --recurse-submodules https://github.com/grpc/grpc.git \
    && cd grpc && mkdir -p cmake/build && cd cmake/build \
    && cmake ../../ \
    -DgRPC_INSTALL=ON \
    -DgRPC_BUILD_TESTS=OFF \
    -DgRPC_BUILD_GRPC_RUBY_PLUGIN=OFF \
    -DgRPC_BUILD_GRPC_PYTHON_PLUGIN=OFF \
    -DgRPC_BUILD_GRPC_PHP_PLUGIN=OFF \
    -DgRPC_BUILD_GRPC_OBJECTIVE_C_PLUGIN=OFF \
    -DgRPC_BUILD_GRPC_NODE_PLUGIN=OFF \
    -DgRPC_BUILD_GRPC_CSHARP_PLUGIN=OFF \
    && make -j4 && make install \
    && cd ../../ && mkdir -p third_party/abseil-cpp/cmake/build \
    && cd third_party/abseil-cpp/cmake/build \
    && cmake -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE ../.. \
    && make -j4 && make install \
    && cd ../../../../../ \
    && rm -rf grpc
