cmake_minimum_required (VERSION 3.0)

project(SWASHES)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

if(UNIX)
    set(CMAKE_CXX_FLAGS "-g -Wall -pedantic -O3")
endif(UNIX)

if(APPLE)
    set(CMAKE_INSTALL_NAME_DIR @executable_path)
    set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)
endif(APPLE)

# includes and source files
include_directories(Headers)
include_directories(Sources)
file(GLOB SWASHES_SOURCES Sources/*.cpp)

# executable
add_executable(swashes ${SWASHES_SOURCES})
target_compile_definitions(swashes PRIVATE CLE=TRUE)

if(WIN32)
    target_link_libraries(swashes)
else(WIN32)
    target_link_libraries(swashes m pthread)
endif(WIN32)

# install
install(TARGETS swashes DESTINATION bin)
