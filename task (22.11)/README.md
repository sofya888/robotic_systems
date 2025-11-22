Компиляция и запуск

# Компиляция всех примеров
g++ -o file_ops file_operations.cpp
g++ -o proc_read proc_filesystem.cpp
g++ -o sparse_create sparse_file.cpp
g++ -o file_lock file_locking.cpp
g++ -o file_copy file_copy.cpp

# Запуск
./file_ops
./proc_read
./sparse_create
./file_lock
./file_copy source.txt destination.txt
