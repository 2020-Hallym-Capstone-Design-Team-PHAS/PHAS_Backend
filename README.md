### PHAS Backend

#### 개발 환경
```
Ubuntu 18.04 LTS
docker 19.03.8
docker-compose 1.17.1
django 3.0.5
Python 3.8.2
postgresql 12.04
travis-ci
```

#### Directory 구조
```
├── docker
│   └── data
├── Docker
├── docker-compose.yml
├── Dockerfile
├── heartbeat
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── LICENSE
├── manage.py
├── phas_server
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── start
└── users
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    ├── models.py
    ├── __pycache__
    ├── tests.py
    ├── urls.py
    └── views.py

```

### API 구현 현황
![image](https://user-images.githubusercontent.com/29707967/80556009-1b924480-8a0d-11ea-9ccc-6970f3f1e8c7.png)
[PHAS API](https://www.notion.so/95e79c15df5640fa875fb6f04c856ce1)

### 개발 현황
*   [x] __docker, docker-compose 를 활용해 django, postgresql 컨테이너 연동 완료__
*   [x] __django를 활용한 API 구현 50% 완료__
*   [x] __[Travis-ci](travis-ci.org)를 활용한 CI 구현 완료__


### 사용법
1.  `sudo apt-get install docker`
2.  `sudo apt-get install docker-composer`
3.  `docker-composer build`
4.  `docker-composer up -d` 
   *    `background`에서 실행하고 싶다면 `-d` 옵션 추가. 아니면 빼도 상관없음.
