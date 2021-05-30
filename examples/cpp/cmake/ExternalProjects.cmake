include(FetchContent)

FetchContent_Declare(
    gRPC
    GIT_REPOSITORY https://github.com/grpc/grpc.git
    GIT_TAG v1.38.0
    GIT_SUBMODULES_RECURSE ON
    GIT_SHALLOW ON
)

set(FETCHCONTENT_QUIET OFF)
FetchContent_MakeAvailable(gRPC)
