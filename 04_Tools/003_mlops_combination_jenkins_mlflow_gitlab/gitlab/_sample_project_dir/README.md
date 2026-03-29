

## 파일 안내  

|파일명|설명|
|---|---|
|.gitignore|- 파일들의 경로(path)별로 특정 속성(attribute)를 지정하는 설정 파일<br>- 이를 통해 Git이 특정 파일들을 어떻게 처리해야 할지 제어할 수 있다.<br>- e.g. 줄바꿈 방식 -> 특정 파일은 CRLF, 특정 파일은 LF<br>- e.g. Git LFS 파일 지정|
|.gitattributes||

### .gitattributes 파일  

```bash
# .psd 파일은 Git LFS로 추적
*.psd filter=lfs diff=lfs merge=lfs -text

# 모델 파일들도 LFS로 관리
models/*.pth filter=lfs diff=lfs merge=lfs -text

# 모든 텍스트 파일은 Git에 저장(commit)될 때 LF로 변환하고,
# 내 작업 공간(working directory)으로 가져올(checkout) 때는 시스템 기본값으로 맞춤.
* text=auto

# 특정 파일들은 항상 LF로 유지
*.sh text eol=lf

# 특정 파일들은 항상 CRLF로 유지
*.bat text eol=crlf
```


## 설정 안내  

|설정|설정|설명|경로|
|---|---|---|---|
|Git LFS|ON|대용량 저장소.|General > Visibility..|
|||||