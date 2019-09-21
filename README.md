# Validation

Validation helps you get validation from the world(read: twitter). You can "validate" what the world thinks (read: sentiment analysis) about a particular topic (ex: pineapple on pizza/crocs on socks/donald trump etc.) and settle arguments with real data and graphs!

This was demoed in ShellHacks 2018 in Miami, FL.
## Setup

Clone the repository

```bash
git clone https://github.com/debdeepB/validation.git
cd validation
```

The frontend is written in Vue.js and the backend is written in Django. Run two servers in different ports.

For frontend:

```bash
cd frontend
yarn install
yarn serve
```

This starts the frontend server at port 8080

For backend:

create a virtual environment

```bash
cd backend
virtualenv venv
source venv/bin/activate
```

pip install the dependencies

```bash
pip install -r requirements.txt
```

Run the backend web-server at port 8002
```bash
python manage.py runserver 127.0.0.1:8002
```









