import socket
import tqdm
import os


def send_file(host, port, file_path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    file_size = os.path.getsize(file_path)
    s.send(f"{file_size}".encode())

    progress = tqdm.tqdm(range(file_size),f"Jo'natilmoqda: {file_path}",unit = "B",unit_scale = True,unit_divisor = 1024)
    
    with open(file_path, 'rb') as f:

        while True:
            data = f.read(1024)
            if not data:
                break
            s.sendall(data)
            progress.update(len(data))
        print("Fayl jo'natildi")
        f.close()
    s.close()


if __name__ == "__main__":
    send_file('10.252.39.32', 12345, 'F:\\klent_server\\img.png')
