import socket, time, sys
host, port = "db", 3306
for i in range(60):  # รอสูงสุด ~120 วินาที
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))
        s.close()
        print("DB is up")
        sys.exit(0)
    except Exception as e:
        print("waiting for db...", e)
        time.sleep(2)
print("DB not reachable")
sys.exit(1)
