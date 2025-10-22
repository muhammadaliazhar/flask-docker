# Deploy Python Flask App on Docker Container

# Step 1

```bash
 git clone https://github.com/muhammadaliazhar/PythonApp-docker.git
```

# Step 2

```bash
docker build -t flask-app .
```

# Step 3

```bash
docker run -d -p 80:80 flask-app
```

<img width="1666" height="211" alt="image" src="https://github.com/user-attachments/assets/5514175a-45c9-4883-be6a-f2dfc4f44056" />


# Step 4

Open port 80 on your instance security group ( firewall rule )

Hit public ip of your instance on a browser

<img width="1156" height="559" alt="image" src="https://github.com/user-attachments/assets/1f99809b-6798-4189-90cd-7f1dbe660990" />

<img width="582" height="404" alt="image" src="https://github.com/user-attachments/assets/26fa2eef-3551-450b-9d47-5cfa5f11ee7c" />

# Step 5

Check container logs
```bash
docker logs <container-id>
```

<img width="1513" height="441" alt="image" src="https://github.com/user-attachments/assets/8cbfdfc4-7020-4956-b3f7-c91ecd4cca86" />

# Real-time container logs
To see real time logs of a docker container we use attach command, this will attach our host terminal with the container terminal

```bash
docker attach <container-id
```







