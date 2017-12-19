# for some reason, obj is not created/extracted with conda-build
mkdir -p obj
make
install -t $PREFIX/bin bin/swashes
