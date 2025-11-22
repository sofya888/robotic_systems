# Задание 22.11

## Компиляция и запуск (WSL/Ubuntu)

Откройте PowerShell и войдите в WSL:
wsl

# Внутри WSL (Ubuntu):
```
cd "/mnt/c/Users/sofus/robotic_systems/task (22.11)/src"
sudo apt-get update
sudo apt-get install -y g++
````
# Компиляция
g++ -std=c++17 -O2 -o file_ops     file_operations.cpp
g++ -std=c++17 -O2 -o proc_read    proc_filesystem.cpp
g++ -std=c++17 -O2 -o sparse_create sparse_file.cpp
g++ -std=c++17 -O2 -o file_lock    file_locking.cpp
g++ -std=c++17 -O2 -o file_copy    file_copy.cpp

# Запуск
./file_ops
./proc_read
./sparse_create
./file_lock

# Для копирования создайте исходный файл и запустите утилиту:
echo "sample data" > source.txt
./file_copy source.txt destination.txt
