MKDIR obj
gnumake.exe -e CC=msvc
COPY bin\swashes %PREFIX%\bin
