cmake.exe -DCMAKE_BUILD_TYPE=Release CMakeLists.txt
cmake.exe --build .
COPY bin\swashes %PREFIX%\bin
