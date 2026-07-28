## 실행 방법  

### 1. 환경변수 파일 편집  

- `.env` 파일을 열고 수정이 필요한 부분을 수정합니다.  

### 2. docker-compose up  

- `docker-compose up -d` 명령어를 통해 docker compose 파일에 정의된 컨테이너를 실행시킵니다.  



## Trouble Shooting  

### Jenkins mount 디렉터리 에러  

#### 에러 메시지  

```bash
INSTALL WARNING: User:  missing rw permissions on JENKINS_HOME: /var/jenkins_home
touch: cannot touch '/var/jenkins_home/copy_reference_file.log': Permission denied
```

#### 원인  

- 이미 호스트에 동일 디렉터리가 있는 경우, 권한 불일치로 인함  

#### 해결  

- 호스트에 있는 jenkins 마운트 디렉터리를 제거한 뒤 docker-compose up 재실행  


