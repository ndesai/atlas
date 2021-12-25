cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(AtlasCppExample)

# Include dependencies
include(cmake/ExternalProjects.cmake)

# When build your project in RelWithDebugInfo configuration,
# try to use Release configuration of the *IMPORTED* libraries.
# If some IMPORTED library has no Release configuration, fallback to Debug one.
# set(CMAKE_MAP_IMPORTED_CONFIG_RELWITHDEBUGINFO Release Debug)

# Protobuf
# set(protobuf_MODULE_COMPATIBLE TRUE)
# find_package(protobuf REQUIRED)
# message(STATUS "Using protobuf ${protobuf_VERSION}")

# # gRPC
# find_package(gRPC REQUIRED)
# message(STATUS "Using gRPC ${gRPC_VERSION}")

# # gRPC C++ plugin
# get_target_property(gRPC_CPP_PLUGIN_EXECUTABLE gRPC::grpc_cpp_plugin
#     IMPORTED_LOCATION_RELEASE)

# Proto file
# get_filename_component(rg_proto ${CMAKE_CURRENT_LIST_DIR}/protos/helloworld.proto ABSOLUTE)
# get_filename_component(rg_proto_path "${rg_proto}" PATH)

# add_custom_command(
#       OUTPUT "${rg_proto_srcs}" "${rg_proto_hdrs}" "${rg_grpc_srcs}" "${rg_grpc_hdrs}"
#       COMMAND ${_PROTOBUF_PROTOC}
#       ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
#         --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
#         -I "${rg_proto_path}"
#         --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
#         "${rg_proto}"
#       DEPENDS "${rg_proto}")


# protoc --cpp_out=$PWD/cpp --plugin=protoc-gen-grpc=/usr/local/bin/grpc_cpp_plugin --grpc_out=$PWD/cpp --proto_path=../../examples/cpp/protos/ ../../examples/cpp/protos/*

set(LIB_HEADERS
    src/Service.h
)

set(LIB_SOURCES
    src/Service.cpp
)

add_library(AtlasCppExampleLibrary
    ${LIB_SOURCES}
    ${LIB_HEADERS}
)

add_executable(${PROJECT_NAME}
    src/main.cpp
)

target_link_libraries(
    ${PROJECT_NAME}
    AtlasCppExampleLibrary
    grpc++
)
