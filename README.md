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

### API 구현 현황
![image](https://user-images.githubusercontent.com/29707967/82773860-1c888b80-9e7e-11ea-881e-a66bb5f8ad3f.png)
[PHAS API](https://www.notion.so/95e79c15df5640fa875fb6f04c856ce1)

### 개발 현황
*   [x] __docker, docker-compose 를 활용해 django, postgresql 컨테이너 연동 완료__
*   [x] __django를 활용한 API 구현 100% 완료__
*   [x] __[Travis-ci](travis-ci.org)를 활용한 CI 구현 완료__

### 각종 Document 및 참고 자료 사이트
*   [django Document](https://docs.djangoproject.com/en/3.0/)    
*   [docker Document](https://docs.docker.com/)    
*   [docker를 활용한 개발환경 구성](https://www.44bits.io/ko/post/almost-perfect-development-environment-with-docker-and-docker-compose#%EA%B7%B8%EB%9F%B0%EB%8D%B0-%EC%95%B1-%EC%84%9C%EB%B9%84%EC%8A%A4%EC%97%90%EC%84%9C-db-%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%B0%BE%EC%95%98%EC%A7%80)   
*   [docker를 사용하는 이유](https://www.44bits.io/ko/post/easy-deploy-with-docker)
*   [docker compose를 사용한 개발환경 구축](https://www.44bits.io/ko/post/almost-perfect-development-environment-with-docker-and-docker-compose#%EA%B7%B8%EB%9F%B0%EB%8D%B0-%EC%95%B1-%EC%84%9C%EB%B9%84%EC%8A%A4%EC%97%90%EC%84%9C-db-%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%B0%BE%EC%95%98%EC%A7%80)
*   [docker로 자신의 이미지 만들어 배포 하기](https://siner308.github.io/2019/02/25/django-docker-custom-image/)


### 실행 방법
*   `sudo apt-get install docker`
*   `sudo apt-get install docker-composer`
*   `docker-composer build`
*   `docker-composer up -d` 
    *   `background`에서 실행하고 싶다면 `-d` 옵션 추가. 아니면 빼도 상관없음.
