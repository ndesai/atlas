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
    && ./bootstrap -- -DCMAKE_BUILD_TYPE:STRING=Release && make && make install \
    && cd ../ && rm -rf cmake-${CMAKE_VERSION}*

RUN apt -y update && \
    apt -y install autoconf libtool pkg-config
