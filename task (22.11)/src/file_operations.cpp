#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>
#include <cstring>
#include <cerrno>

using namespace std;

void basic_fd_example() {
    int file_descriptor = open("example.txt", O_CREAT | O_WRONLY, 0644);
    if (file_descriptor == -1) {
        cerr << "Ошибка открытия файла: " << strerror(errno) << endl;
        return;
    }
    const char* message = "Hello, File Descriptors!\\n";
    ssize_t bytes_written = write(file_descriptor, message, strlen(message));
    if (bytes_written == -1) {
        cerr << "Ошибка записи: " << strerror(errno) << endl;
    }
    close(file_descriptor);
}

void demonstrate_file_operations() {
    // Создание и запись в файл
    int fd = open("test_file.txt", O_CREAT | O_RDWR, 0644);
    if (fd != -1) {
        write(fd, "Test data", 9);

        // SEEK_SET — от начала файла
        lseek(fd, 0, SEEK_SET);

        char buffer[100];
        ssize_t bytes_read = read(fd, buffer, sizeof(buffer) - 1);
        if (bytes_read >= 0) {
            buffer[bytes_read] = '\\0';
            cout << "Прочитано: " << buffer << endl;
        }
        close(fd);
    }

    // Метаданные файла
    struct stat file_info;
    if (stat("test_file.txt", &file_info) == 0) {
        cout << "Размер файла: " << file_info.st_size << " байт" << endl;
        cout << "Владелец (uid): " << file_info.st_uid << endl;
        cout << "Права доступа (oct): " << oct << file_info.st_mode << dec << endl;
    }

    // Содержимое каталога
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
    cout << "Изучаем низкоуровневый ввод-вывод в Linux" << endl;
    basic_fd_example();
    demonstrate_file_operations();
    return 0;
}
