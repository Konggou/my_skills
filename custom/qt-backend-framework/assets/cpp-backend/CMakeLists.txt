cmake_minimum_required(VERSION 3.16)

project(BackendDemo VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(MSVC)
    add_compile_options(/utf-8)
endif()

set(CMAKE_AUTOMOC ON)

find_package(Qt6 QUIET COMPONENTS Core)
if(Qt6_FOUND)
    set(QT_VERSION_MAJOR 6)
    set(QT_CORE_TARGET Qt6::Core)
else()
    find_package(Qt5 REQUIRED COMPONENTS Core)
    set(QT_VERSION_MAJOR 5)
    set(QT_CORE_TARGET Qt5::Core)
endif()

add_library(backend STATIC
    model/appmodel.h
    service/appservice.h
    service/appservice.cpp
    controller/maincontroller.h
    controller/maincontroller.cpp
)

target_include_directories(backend PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(backend PUBLIC ${QT_CORE_TARGET})
