

## System Requiremetns  

<i>2024.01.14 Dart 3.2.4 version 기준</i>

|OS|항목|requirements|
|---|---|---|
|Windows|OS|Windows 10 and 11.|
||architectures|x64, IA32, ARM64.|
|Mac OS|OS|Mac OS 12, 13, 14|
||architectures|x64, ARM64.|
|Linux|OS|Debian stable, Ubuntu LTS|
||architectures|x64, IA32, ARM64, ARM, RISC-V (RV64GC).|

<i>Windows : Support for ARM64 is in preview, and is available only in the dev and beta channels.</i>  
<i>Linux : Support for RISC-V is in preview, and is available only in the dev and beta channels.</i>  


## Dart SDK install  

[https://dart.dev/get-dart](https://dart.dev/get-dart)  

(1) Mac OS  

```zsh
# install
brew tap dart-lang/dart
brew install dart

# upgrade  
brew upgrade dart

# 버전 변경  
brew install dart@신규버전
brew unlink dart@기존버전
brew unlink dart@신규버전
brew link dart@신규버전

# dart 정보 표시
brew info dart

==> dart-lang/dart/dart: stable 3.2.4, HEAD
SDK ...
```

(2) Windows  

```cmd
REM install
choco install dart-sdk

REM upgrade
choco upgrade dart-sdk
```

(3) Linux

```bash
# install
sudo apt-get update
sudo apt-get install apt-transport-https
wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/dart.gpg
echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | sudo tee /etc/apt/sources.list.d/dart_stable.list

sudo apt-get update
sudo apt-get install dart
```


## Dart Pad  

별도로 Dart SDK를 설치하지 않고 웹브라우저에서 Dart 를 연습할 수 있는 곳.  
[https://dartpad.dev/?](https://dartpad.dev/?)  


## Reference  

dart Docs : https://dart.dev/get-dart  
노마드코더 : https://nomadcoders.co/dart-for-beginners/lectures/4092  