# Mac下Clion配置C++图形图像开发环境

## Qt
### Qt 安装
本想使用tuna上的Qt资源，结果发现配置很麻烦，不如

	brew install qt

有些尴尬

### Qt 配置
找到Qt的安装路径

```cmake
cmake_minimum_required(VERSION 3.9)
project(untitled1)
set(CMAKE_CXX_STANDARD 11)
add_executable(untitled1 main.cpp)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# 设置自动生成moc文件,AUTOMOC打开可以省去QT5_WRAP_CPP命令
set(CMAKE_AUTOMOC ON)
# 打开全局rcc
set(CMAKE_AUTORCC ON)
# 设置自动生成ui.h文件,AUTOUIC打开可以省去QT5_WRAP_UI命令
set(CMAKE_AUTOUIC ON)
set (CMAKE_PREFIX_PATH "/usr/local/Cellar/qt/5.13.0/lib/cmake")
find_package(Qt5Widgets REQUIRED)
find_package(Qt5Quick REQUIRED)
find_package(Qt5Core REQUIRED)
target_link_libraries(untitled1 Qt5::Quick)
target_link_libraries(untitled1 Qt5::Widgets)
target_link_libraries(untitled1 Qt5::Core)
```

这样Qt就搞定辣！

### QtDesigner

Preferences--->Tools--->External Tools

新建一个外部工具

Program：Designer的路径

Arguments:\$FileName\$

Work directory:\$FileDir\$

### Cmake简介
里面写了Cmake,这里简单介绍一下
首先有几点注意

- CMakeLists.txt文件中不区分大小写


#### 常用命令
- cmake\_minimum\_required(version 3.4.1)指定 cmake 的最小版本
- project(project_name)    定义工程名称
- add\_executable(demo demo.cpp) 生成可执行文件
- add\_library(common STATIC util.cpp) # 生成静态库
- add_library(common SHARED util.cpp) # 生成动态库或共享库

		在 Linux 下是：
		demo
		libcommon.a
		libcommon.so
		在 Windows 下是：
		demo.exe
		common.lib
		common.dll
- add\_library(demo demo.cpp test.cpp util.cpp)明确指定包含哪些源文件
- aux\_source\_directory(. SRC_LIST) # 搜索当前目录下的所有.cpp文件
- add\_library(demo ${SRC_LIST})
- find\_library(VAR name path)查找到指定的预编译库，并将它的路径存储在变量中。
- target\_link\_libraries( #目标库 #目标库要链接的库)
- include_directories(目录) 设置包含的目录
- link_directories(目录) 设置链接的目录
- set 直接设置变量的值
- message("build with debug mode")打印信息
- include(./common.cmake) 包含其他cmake
- 逻辑判断和比较：

		if (expression)：expression 不为空（0,N,NO,OFF,FALSE,NOTFOUND）时为真
		if (not exp)：与上面相反
		if (var1 AND var2)
		if (var1 OR var2)
		if (COMMAND cmd)：如果 cmd 确实是命令并可调用为真
		if (EXISTS dir) if (EXISTS file)：如果目录或文件存在为真
		if (file1 IS_NEWER_THAN file2)：当 file1 比 file2 新，或 file1/file2 中有一个不存在时为真，文件名需使用全路径
		if (IS_DIRECTORY dir)：当 dir 是目录时为真
		if (DEFINED var)：如果变量被定义为真
		if (var MATCHES regex)：给定的变量或者字符串能够匹配正则表达式 regex 时为真，此处 var 可以用 var 名，也可以用 ${var}
		if (string MATCHES regex)
		
		数字比较：
		if (variable LESS number)：LESS 小于
		if (string LESS number)
		if (variable GREATER number)：GREATER 大于
		if (string GREATER number)
		if (variable EQUAL number)：EQUAL 等于
		if (string EQUAL number)
		
		字母表顺序比较：
		if (variable STRLESS string)
		if (string STRLESS string)
		if (variable STRGREATER string)
		if (string STRGREATER string)
		if (variable STREQUAL string)
		if (string STREQUAL string)
	
- 循环控制
		while(condition)
		    ...
		endwhile()
		
		foreach(loop_var RANGE start stop [step])
		    ...
		endforeach(loop_var)
### 预定义变量
- PROJECT\_SOURCE\_DIR：工程的根目录
- PROJECT\_BINARY\_DIR：运行 cmake 命令的目录，通常是 ${PROJECT_SOURCE_DIR}/build
- PROJECT\_NAME：返回通过 project 命令定义的项目名称
- CMAKE\_CURRENT\_SOURCE_DIR：当前处理的CMakeLists.txt 所在的路径
- CMAKE\_CURRENT\_BINARY\_DIR：target 编译目录
- CMAKE\_CURRENT\_LIST\_DIR：CMakeLists.txt 的完整路径
- CMAKE\_CURRENT\_LIST\_LINE：当前所在的行
- CMAKE\_MODULE\_PATH：定义自己的 cmake 模块所在的路径，SET(CMAKE\_MODULE\_PATH ${PROJECT\_SOURCE\_DIR}/cmake)，然后可以用INCLUDE命令来调用自己的模块
- EXECUTABLE\_OUTPUT\_PATH：重新定义目标二进制可执行文件的存放位置
- LIBRARY\_OUTPUT\_PATH：重新定义目标链接库文件的存放位置
		
- BUILD\_SHARED\_LIBS：这个开关用来控制默认的库编译方式，如果不进行设置，使用 add\_library 又没有指定库类型的情况下，默认编译生成的库都是静态库。如果 set(BUILD_SHARED_LIBS ON) 后，默认生成的为动态库
- CMAKE\_C\_FLAGS：设置 C 编译选项，也可以通过指令 add_definitions() 添加
- CMAKE\_CXX\_FLAGS：设置 C++ 编译选项，也可以通过指令 add_definitions() 添加

## OpenCV
虽然python版OpenCV环境已经配好，但是还是需要C++下的OpenCV

[https://opencv.org/releases/](https://opencv.org/releases/)

下载opencv-4.1.1

打开CMake，填好OpenCV路径和build的路径->configure->Done->等->Generate

打开终端，用cd命令进入build文件夹目录，然后输入命令

make

然后

sudo make install

find\_package opencv

最后将OpenCV\_LIBS target\_link\_libraries到项目上

## VTK
同OpenCV

[https://vtk.org/download/](https://vtk.org/download/)

## CMakeLists.txt
```makefile
cmake_minimum_required(VERSION 3.9)
project(untitled1)
set(CMAKE_CXX_STANDARD 11)
add_executable(${PROJECT_NAME}  main.cpp)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)
set (CMAKE_PREFIX_PATH "/usr/local/Cellar/qt/5.13.0/lib/cmake")
find_package(Qt5Widgets REQUIRED)
find_package(Qt5Quick REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(OpenCV REQUIRED)
find_package(VTK REQUIRED)
include(${VTK_USE_FILE})
target_link_libraries(${PROJECT_NAME} Qt5::Quick)
target_link_libraries(${PROJECT_NAME} Qt5::Widgets)
target_link_libraries(${PROJECT_NAME} Qt5::Core)
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
target_link_libraries(${PROJECT_NAME} ${VTK_LIBRARIES})
```

