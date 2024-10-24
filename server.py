import socket
import tqdm

def start_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Server {host}:{port} da ishlamoqda...")
    
    conn, addr = s.accept()
    print(f"Ulangan: {addr}")
    
    # Faylni qabul qilish jarayoni
    received_file_size = int(conn.recv(1024).decode())
    print(f"Qabul qilinadigan fayl hajmi: {received_file_size} bayt")
    
    progress = tqdm.tqdm(range(received_file_size), f"Qabul qilinmoqda", unit="B", unit_scale=True, unit_divisor=1024)
    
    with open('data.zip', 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
            progress.update(len(data))
        print("Fayl qabul qilindi")
        f.close()
    
    conn.close()
    s.close()
    

if __name__ == "__main__":
    start_server('10.252.39.32', 12345)
