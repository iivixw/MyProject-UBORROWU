# MyProject-UBORROWU

##.\venv\Scripts\activate

##python manage.py runserver

##pip install celery

##pip install django-allauth

##pip install django-qr-code

##เปิด settings.py

##แก้ไข MIDDLEWARE เพิ่ม

##'allauth.account.middleware.AccountMiddleware',

##pip install PyJWT

##pip install cryptography

##pip install mlxtend

##pip install apscheduler

##python manage.py makemigrations myappstaff

##python manage.py migrate

# MyProject-UBORROWU

โปรเจกต์ **Django + MariaDB** รันด้วย **Docker Compose**  
ทดสอบแล้ว: `docker compose up -d` ใช้งานได้ และเข้าเว็บที่ `http://localhost:9052`

---

## โครงสร้างที่ใช้รัน
- `docker-compose.yml` – orchestration สำหรับ `web` (Django) + `db` (MariaDB)
- `Dockerfile` – สร้างอิมเมจ Django
- `.env` – ตัวแปรแวดล้อม (เช่น `DATABASE_URL`, `DJANGO_SECRET_KEY`)
- `wait-for.sh` – สคริปต์รอ DB พร้อมก่อนสตาร์ต Django
- โค้ด Django ทั้งหมด (`manage.py`, แอปต่างๆ)

> หมายเหตุ: **อย่า commit รหัสผ่านจริง/คีย์จริง** ลง `.env` ใน repo สาธารณะ

---

## ข้อกำหนดเบื้องต้น
- ติดตั้ง **Docker Desktop** (แนะนำใช้ WSL2 หากเป็น Windows 10/11)
- Docker Compose v2 (มากับ Docker Desktop)

ตรวจสอบ:
```bash
docker version

git init

git add .

git commit -m "Init: Dockerized Django + compose + README + full .gitignore"

git branch -M main

git remote add origin https://github.com/iivixw/MyProject-UBORROWU.git

git push -u origin main
