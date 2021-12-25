include(FetchContent)

FetchContent_Declare(
    gRPC
    GIT_REPOSITORY https://github.com/grpc/grpc.git
    GIT_TAG v1.38.0
    GIT_SUBMODULES_RECURSE ON
    GIT_SHALLOW ON
    CMAKE_ARGS -DgRPC_INSTALL=ON
    CMAKE_ARGS -DgRPC_BUILD_TESTS=OFF
    CMAKE_ARGS -DgRPC_PROTOBUF_PROVIDER=package
    CMAKE_ARGS -DgRPC_ZLIB_PROVIDER=package
    CMAKE_ARGS -DgRPC_CARES_PROVIDER=package
    CMAKE_ARGS -DgRPC_SSL_PROVIDER=package
)

set(FETCHCONTENT_QUIET OFF)
FetchContent_MakeAvailable(gRPC)
