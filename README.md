# Deploy Python Flask App on Docker Container

# Step 1

```bash
 git clone https://github.com/muhammadaliazhar/flask-docker.git
```

# Step 2

```bash
docker build -t flask-app .
```

# Step 3

```bash
docker run -d -p 80:80 flask-app
```

# Step 4

Open port 80 on your instance security group ( firewall rule )

Hit public ip of your instance on a browser

<img width="1156" height="559" alt="image" src="https://github.com/user-attachments/assets/1f99809b-6798-4189-90cd-7f1dbe660990" />


