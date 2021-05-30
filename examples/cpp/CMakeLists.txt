cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(AtlasCppExample)

# Include dependencies
include(cmake/ExternalProjects.cmake)

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
