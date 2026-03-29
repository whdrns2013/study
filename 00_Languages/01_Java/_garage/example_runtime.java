package Java._garage;

import java.io.IOException;

public class example_runtime {
    public static void main(String[] args) throws InterruptedException, IOException{
    // try {
    //     // 외부 프로세스 실행
    //     Process p = Runtime.getRuntime().exec("ping https://whdrns2013.github.io");
        
    //     int i = 0;

    //     while (p.isAlive() & i <= 10) {
    //         System.out.println("External process is running...");
    //         Thread.sleep(1000);
    //         i++;
    //     }

    //     // 외부 프로세스가 종료되었을 때 실행
    //     int exitCode = p.exitValue();
    //     System.out.println("External process exited with code: " + exitCode);

    // } catch (IOException e) {
    //     e.printStackTrace();
    
    // }
    // 계속 켜져있는 블로그 프로세스를 외부 프로세스로 바라보도록 하고
    Process p = Runtime.getRuntime().exec("ping https://whdrns2013.github.io");

    int i = 1;

    // While : 프로세스가 살아있다면(true) 그리고 i 가 5 이하라면
    for (int n = 1; n <=6; n++){
    if (p.isAlive() & i <= 5){
      System.out.println("External process is running..."); // 정해진 문구 출력
      Thread.sleep(1000);                                   // 1000ms (1초) 대기
      i++;                                                  // i에 1을 더함
    } else if (p.isAlive() == false & i == 6){
        System.out.println("External process exited with code: " + p.exitValue());
        Thread.sleep(1000);
    }
    }

    // 프로세스가 종료되었을 때 종료코드 출력
    if (p.isAlive() & i == 6){
        System.out.println("External process exited with code: " + p.exitValue());
    }
}
}
