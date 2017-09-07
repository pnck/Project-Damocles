cmake_minimum_required(VERSION 3.7)
project(Project_Damocles)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
    CQPdemo/appmain.cpp
    CQPdemo/appmain.h
    CQPdemo/cqp.h
    CQPdemo/dllmain.cpp
    #CQPdemo/pw.libc.Damocles.json
    CQPdemo/stdafx.cpp
    CQPdemo/stdafx.h
    CQPdemo/targetver.h)

add_executable(Project_Damocles ${SOURCE_FILES})