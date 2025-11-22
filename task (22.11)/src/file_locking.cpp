#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/file.h>
#include <cstring>

using namespace std;

void demonstrate_file_locking() {
    const char* filename = "locked_file.txt";
    int fd = open(filename, O_CREAT | O_RDWR, 0644);
    if (fd == -1) {
        perror("open");
        return;
    }

    const char* data = "Hello World!";
    write(fd, data, strlen(data));

    struct flock lock;
    lock.l_type = F_WRLCK;
    lock.l_whence = SEEK_SET;
    lock.l_start = 0;
    lock.l_len = 5;
    lock.l_pid = getpid();

    if (fcntl(fd, F_SETLK, &lock) == -1) {
        cout << "Не удалось установить блокировку" << endl;
    } else {
        cout << "Блокировка установлена на первые 5 байт" << endl;
        sleep(5);
        lock.l_type = F_UNLCK;
        fcntl(fd, F_SETLK, &lock);
        cout << "Блокировка снята" << endl;
    }
    close(fd);
}

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
        if (fcntl(fd, F_SETLKW, &lock) != -1) {
            cout << "Дочерний процесс получил блокировку" << endl;
            sleep(2);
            lock.l_type = F_UNLCK;
            fcntl(fd, F_SETLK, &lock);
        }
        close(fd);
    } else {
        // Родительский процесс
        sleep(1);
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
    cout << "\\n=== Демонстрация конкурентного доступа ===" << endl;
    concurrent_access_example();
    return 0;
}
