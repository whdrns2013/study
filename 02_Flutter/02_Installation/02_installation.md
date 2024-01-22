

## Installation  

Flutter.dev 사이트로 가 Install을 진행한다.  

[https://docs.flutter.dev/get-started/install](https://docs.flutter.dev/get-started/install)  

운영체제에 맞는 것은 선택 해 다운로드 후 설치를 해준다.  

이건 두 단계로 이루어져있는데,  

(1) SDK 설치 : Dart, 및 기타 개발에 필요한 개발 도구를 설치한다.  
(2) 시뮬레이터 설치 : ...


하지만 이렇게 설치하는 것을 권장하지는 않는다. 아래를 보자.  


## SDK Installation  

### Windows  

chocolatey 를 이용해 설치한다. chocolatey는 Windows에서 뭔갈 설치할 수 있게 해주는 패키지 매니저이다.  

zip 파일을 다운로드 받을 필요도 없고, path 설정을 따로 해줄 필요도 없다.  

[https://chocolatey.org/install](https://chocolatey.org/install)  

위 링크로 chocolatey.org/install 로 이동해서 패키지를 설치할 것이다.  

**choco가 설치된 경우, 1~4번은 skip 해도 된다**  

1. Choose How to Install Chocolatey  
-> individual 선택  

2. PowerShell 을 설치해준다.  

3. PowerShell 을 관리자 권한으로 열고

4. chocolatey에서 안내하는 대로 설치를 진행한다.  

```powershell
Get-ExecutionPolicy
# >> Restricted

Set-ExecutionPolicy AllSigned

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

5. choco를 통해 flutter SDK를 설치한다.  

```powershell
choco install flutter
```


### Mac OS  

Mac OS 사용자들은 친숙한 HomeBrew를 이용한다.  



1. homebrew 를 설치한다.  

2. 터미널에 아래 명령어를 입력해 Flutter SDK를 설치한다.  

(주의) 원활한 설치를 위해서는 기존 설치한 dart를 삭제하고 flutter를 설치하는 것을 추천함  
flutter SDK에 dart 또한 포함되어있음.  

```zsh
brew install --cask flutter
```



## Simulator Installation  

### Windows  

windows, web, android 세 가지 선택지가 있다.  
웹을 개발하려고 한다면 딱히 할 것은 없다. 이미 브라우저가 있으므로.  

만약 Android 앱을 개발하려고 하면 가이드의 android setup으로 가서 해당 페이지에 있는 설치 방법을 따라 Android Simulator를 설치한다.  

[https://docs.flutter.dev/get-started/install/windows](https://docs.flutter.dev/get-started/install/windows)

또한 윈도우 개발을 원한다면 해당 가이드를 따르자.  

### Mac OS

Mac OS는 여러 선택지가 있다.  

iOS, Android, macOS, Web 까지.  

이 또한 가이드의 내용을 따라 진행하자.  

[https://docs.flutter.dev/get-started/install/macos](https://docs.flutter.dev/get-started/install/macos)  

### 주의할 점  

모든 플랫폼 (iOS, Android, macOS, Web...) 을 한 번에 모두 설치할 필요는 없다.  
그때그때 필요한 경우 설치하면 되는 것이다.  

그러니 모든 것을 다 설치하기 위해 시간을 쏟지 말고, 하나만을 정해서 우선 해보면 된다.  

==> 나는 우선 Web, MacOS, iOS 들을 다운로드 받음