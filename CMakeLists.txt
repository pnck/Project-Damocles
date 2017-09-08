cmake_minimum_required(VERSION 3.7)
project(Project_Damocles)

set(CMAKE_CXX_STANDARD 11)

include_directories("/Windows/Program Files (x86)/Windows Kits/8.1/Include/um")

set(SOURCE_FILES
    CQPdemo/appmain.cpp
    CQPdemo/appmain.h
    CQPdemo/cqp.h
    CQPdemo/dllmain.cpp
    #CQPdemo/pw.libc.Damocles.json
    CQPdemo/stdafx.cpp
    CQPdemo/stdafx.h
    CQPdemo/targetver.h
    CQPdemo/utils.cpp
    CQPdemo/utils.h
    CQPdemo/CqPyHandlerWrapper.cpp
    CQPdemo/CqPyHandlerWrapper.h)

add_executable(Project_Damocles ${SOURCE_FILES})