# Руководство по низкоуровневому вводу-выводу в C++ для Ubuntu

## 1. Обзор механизмов ввода-вывода в ОС Linux

### Основные концепции

```cpp
// Пример: Базовое понимание системных вызовов
#include <iostream>
#include <unistd.h>  // Для системных вызовов POSIX
#include <fcntl.h>   // Для констант файлового доступа
#include <sys/stat.h> // Для работы с метаданными файлов

using namespace std;

int main() {
    // В Linux все является файлом:
    // - Обычные файлы
    // - Каталоги
    // - Устройства (/dev)
    // - Сокеты
    // - Именованные каналы
    
    cout << "Изучаем низкоуровневый ввод-вывод в Linux" << endl;
    return 0;
}
```

## 2. Файлы и файловые дескрипторы

```cpp
#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <cstring>
#include <cerrno>

int main() {
    // Файловый дескриптор - целое число, представляющее открытый файл
    int file_descriptor; 
    
    // open() - системный вызов для открытия/создания файла
    // Параметры:
    // "example.txt" - имя файла
    // O_CREAT | O_WRONLY - флаги:
    //   O_CREAT - создать файл если не существует
    //   O_WRONLY - открыть только для записи
    // 0644 - права доступа (rw-r--r--)
    file_descriptor = open("example.txt", O_CREAT | O_WRONLY, 0644);
    
    if (file_descriptor == -1) {
        // errno - глобальная переменная, содержащая код ошибки
        // strerror - преобразует код ошибки в читаемое сообщение
        cerr << "Ошибка открытия файла: " << strerror(errno) << endl;
        return 1;
    }
    
    const char* message = "Hello, File Descriptors!\n";
    
    // write() - системный вызов для записи в файл
    // Параметры:
    // file_descriptor - дескриптор файла
    // message - указатель на данные для записи
    // strlen(message) - количество байт для записи
    ssize_t bytes_written = write(file_descriptor, message, strlen(message));
    
    if (bytes_written == -1) {
        cerr << "Ошибка записи: " << strerror(errno) << endl;
    }
    
    // close() - закрывает файловый дескриптор
    close(file_descriptor);
    
    return 0;
}
```

## 3. Системные вызовы для работы с файловой системой

```cpp
#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>
#include <cstring>

void demonstrate_file_operations() {
    // Создание и запись в файл
    int fd = open("test_file.txt", O_CREAT | O_RDWR, 0644);
    
    if (fd != -1) {
        write(fd, "Test data", 9);
        
        // lseek() - перемещает указатель позиции в файле
        // SEEK_SET - отсчет от начала файла
        lseek(fd, 0, SEEK_SET);
        
        char buffer[100];
        // read() - чтение из файла
        ssize_t bytes_read = read(fd, buffer, sizeof(buffer) - 1);
        buffer[bytes_read] = '\0';
        
        cout << "Прочитано: " << buffer << endl;
        close(fd);
    }
    
    // Работа с метаданными файлов
    struct stat file_info;
    if (stat("test_file.txt", &file_info) == 0) {
        cout << "Размер файла: " << file_info.st_size << " байт" << endl;
        cout << "Владелец: " << file_info.st_uid << endl;
        cout << "Права доступа: " << oct << file_info.st_mode << dec << endl;
    }
    
    // Работа с каталогами
    DIR* dir = opendir(".");
    if (dir) {
        struct dirent* entry;
        cout << "Файлы в текущем каталоге:" << endl;
        while ((entry = readdir(dir)) != nullptr) {
            cout << "  " << entry->d_name << endl;
        }
        closedir(dir);
    }
}

int main() {
    demonstrate_file_operations();
    return 0;
}
```

## 4. Файловая система proc

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

void read_proc_filesystem() {
    // /proc - виртуальная файловая система
    // Содержит информацию о процессах и системе
    
    // Чтение информации о процессоре
    ifstream cpuinfo("/proc/cpuinfo");
    string line;
    
    cout << "Информация о процессоре:" << endl;
    for (int i = 0; i < 5 && getline(cpuinfo, line); i++) {
        cout << line << endl;
    }
    
    // Чтение информации о памяти
    ifstream meminfo("/proc/meminfo");
    cout << "\nИнформация о памяти:" << endl;
    for (int i = 0; i < 3 && getline(meminfo, line); i++) {
        cout << line << endl;
    }
    
    // Чтение информации о текущем процессе
    string pid = to_string(getpid());
    string stat_path = "/proc/" + pid + "/stat";
    
    ifstream proc_stat(stat_path);
    if (proc_stat) {
        cout << "\nИнформация о процессе " << pid << ":" << endl;
        getline(proc_stat, line);
        cout << line << endl;
    }
}

int main() {
    read_proc_filesystem();
    return 0;
}
```

## 5. Разреженные файлы

```cpp
#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>

void create_sparse_file() {
    // Разреженный файл - файл, в котором пустые блоки не занимают места на диске
    
    const char* filename = "sparse_file.bin";
    
    // Создаем разреженный файл
    int fd = open(filename, O_CREAT | O_WRONLY, 0644);
    
    if (fd == -1) {
        perror("open");
        return;
    }
    
    // Записываем данные в начало файла
    const char* start_data = "START";
    write(fd, start_data, strlen(start_data));
    
    // Перемещаемся на большую позицию (создаем "дыру" в файле)
    off_t offset = 1024 * 1024; // 1 МБ
    lseek(fd, offset, SEEK_CUR);
    
    // Записываем данные в конец файла
    const char* end_data = "END";
    write(fd, end_data, strlen(end_data));
    
    close(fd);
    
    // Проверяем размер файла
    struct stat st;
    stat(filename, &st);
    
    cout << "Размер файла: " << st.st_size << " байт" << endl;
    cout << "Занимаемое место: " << st.st_blocks * 512 << " байт" << endl;
    cout << "Файл разреженный: " << (st.st_blocks * 512 < st.st_size ? "Да" : "Нет") << endl;
}

int main() {
    create_sparse_file();
    return 0;
}
```

## 6. Блокировка областей файла

```cpp
#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/file.h>
#include <cstring>

void demonstrate_file_locking() {
    const char* filename = "locked_file.txt";
    int fd = open(filename, O_CREAT | O_RDWR, 0644);
    
    if (fd == -1) {
        perror("open");
        return;
    }
    
    // Записываем тестовые данные
    const char* data = "Hello World!";
    write(fd, data, strlen(data));
    
    // Определяем структуру для блокировки
    struct flock lock;
    
    // Настраиваем блокировку:
    lock.l_type = F_WRLCK;   // Тип блокировки - запись
    lock.l_whence = SEEK_SET; // Отсчет от начала файла
    lock.l_start = 0;        // Начальная позиция
    lock.l_len = 5;          // Длина блокируемой области (5 байт)
    lock.l_pid = getpid();   // ID процесса
    
    // Устанавливаем блокировку
    if (fcntl(fd, F_SETLK, &lock) == -1) {
        cout << "Не удалось установить блокировку" << endl;
    } else {
        cout << "Блокировка установлена на первые 5 байт" << endl;
        
        // Работа с заблокированной областью
        sleep(5); // Имитация работы
        
        // Снимаем блокировку
        lock.l_type = F_UNLCK;
        fcntl(fd, F_SETLK, &lock);
        cout << "Блокировка снята" << endl;
    }
    
    close(fd);
}

// Пример конкурентного доступа
void concurrent_access_example() {
    pid_t pid = fork();
    
    if (pid == 0) {
        // Дочерний процесс
        int fd = open("test_lock.txt", O_CREAT | O_RDWR, 0644);
        struct flock lock;
        
        lock.l_type = F_WRLCK;
        lock.l_whence = SEEK_SET;
        lock.l_start = 0;
        lock.l_len = 10;
        
        cout << "Дочерний процесс пытается получить блокировку..." << endl;
        if (fcntl(fd, F_SETLKW, &lock) != -1) { // F_SETLKW - ждет блокировку
            cout << "Дочерний процесс получил блокировку" << endl;
            sleep(2);
            lock.l_type = F_UNLCK;
            fcntl(fd, F_SETLK, &lock);
        }
        close(fd);
    } else {
        // Родительский процесс
        sleep(1); // Даем дочернему процессу начать первым
        int fd = open("test_lock.txt", O_CREAT | O_RDWR, 0644);
        struct flock lock;
        
        lock.l_type = F_WRLCK;
        lock.l_whence = SEEK_SET;
        lock.l_start = 0;
        lock.l_len = 10;
        
        cout << "Родительский процесс проверяет блокировку..." << endl;
        if (fcntl(fd, F_GETLK, &lock) != -1) {
            if (lock.l_type == F_UNLCK) {
                cout << "Область не заблокирована" << endl;
            } else {
                cout << "Область заблокирована процессом " << lock.l_pid << endl;
            }
        }
        close(fd);
    }
}

int main() {
    cout << "=== Демонстрация блокировки файлов ===" << endl;
    demonstrate_file_locking();
    
    cout << "\n=== Демонстрация конкурентного доступа ===" << endl;
    concurrent_access_example();
    
    return 0;
}
```

## Полный пример: утилита для копирования файлов

```cpp
#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <cstring>
#include <cerrno>

bool copy_file_lowlevel(const char* source, const char* destination) {
    int src_fd, dst_fd;
    struct stat src_stat;
    char buffer[4096];
    ssize_t bytes_read, bytes_written;
    
    // Открываем исходный файл для чтения
    src_fd = open(source, O_RDONLY);
    if (src_fd == -1) {
        cerr << "Ошибка открытия исходного файла: " << strerror(errno) << endl;
        return false;
    }
    
    // Получаем информацию о исходном файле
    if (fstat(src_fd, &src_stat) == -1) {
        cerr << "Ошибка получения информации о файле: " << strerror(errno) << endl;
        close(src_fd);
        return false;
    }
    
    // Создаем целевой файл с теми же правами
    dst_fd = open(destination, O_CREAT | O_WRONLY | O_TRUNC, src_stat.st_mode);
    if (dst_fd == -1) {
        cerr << "Ошибка создания целевого файла: " << strerror(errno) << endl;
        close(src_fd);
        return false;
    }
    
    // Копируем данные
    while ((bytes_read = read(src_fd, buffer, sizeof(buffer))) > 0) {
        bytes_written = write(dst_fd, buffer, bytes_read);
        if (bytes_written != bytes_read) {
            cerr << "Ошибка записи в целевой файл" << endl;
            close(src_fd);
            close(dst_fd);
            return false;
        }
    }
    
    if (bytes_read == -1) {
        cerr << "Ошибка чтения исходного файла" << endl;
        close(src_fd);
        close(dst_fd);
        return false;
    }
    
    // Закрываем файлы
    close(src_fd);
    close(dst_fd);
    
    cout << "Файл успешно скопирован: " << source << " -> " << destination << endl;
    return true;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cout << "Использование: " << argv[0] << " <исходный_файл> <целевой_файл>" << endl;
        return 1;
    }
    
    if (copy_file_lowlevel(argv[1], argv[2])) {
        return 0;
    } else {
        return 1;
    }
}
```

## Компиляция и запуск

```bash
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
```

## Ключевые моменты для запоминания:

1. **Файловые дескрипторы** - низкоуровневые указатели на открытые файлы
2. **Системные вызовы** - прямое обращение к ядру ОС
3. **Блокировки** - механизм синхронизации доступа к файлам
4. **/proc** - виртуальная ФС для получения информации о системе
5. **Разреженные файлы** - эффективное использование дискового пространства

Это руководство охватывает основные аспекты низкоуровневого ввода-вывода в Linux и предоставляет практические примеры для лучшего понимания.