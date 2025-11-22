#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <cstring>

using namespace std;

void create_sparse_file() {
    const char* filename = "sparse_file.bin";
    int fd = open(filename, O_CREAT | O_WRONLY, 0644);
    if (fd == -1) {
        perror("open");
        return;
    }

    const char* start_data = "START";
    write(fd, start_data, strlen(start_data));

    off_t offset = 1024 * 1024; // 1 МБ
    lseek(fd, offset, SEEK_CUR);

    const char* end_data = "END";
    write(fd, end_data, strlen(end_data));

    close(fd);

    struct stat st;
    if (stat(filename, &st) == 0) {
        cout << "Размер файла: " << st.st_size << " байт" << endl;
        cout << "Занимаемое место: " << (st.st_blocks * 512) << " байт" << endl;
        cout << "Файл разреженный: "
             << ((st.st_blocks * 512) < st.st_size ? "Да" : "Нет") << endl;
    }
}

int main() {
    create_sparse_file();
    return 0;
}
