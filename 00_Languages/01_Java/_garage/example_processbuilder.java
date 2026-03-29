package Java._garage;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class example_processbuilder {
    public static void main(String[] args) throws IOException{

        ProcessBuilder pb1 = new ProcessBuilder("python", "User/Desktop/python_ex.py");



        ProcessBuilder pb = new ProcessBuilder();

        File path = new File("/Users/jongya/Desktop/Workspace/study/Java/_garage/");
        String fileName = "./example_processbuilder.py";

        pb.directory(path);
        pb.command("python", fileName);

        Process p = pb.start();
        System.out.println(p.isAlive());

        BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream(), "UTF-8"));
        String line;
        while ((line = br.readLine()) != null){
            System.out.println(">>> " + line);
        }
        
        System.out.println(pb.command());
        System.out.println(pb.directory());
        System.out.println(pb.environment());
        System.out.println(pb.inheritIO());
        System.out.println(pb.redirectErrorStream());
        // System.out.println(pb.command);

        System.out.println("======================");

        System.out.println(p.getInputStream());
        System.out.println(p.getOutputStream());
        System.out.println(p.getErrorStream());
        System.out.println(p.isAlive());
        System.out.println(p.exitValue());

        p.destroy();


        ProcessBuilder pb2 = new ProcessBuilder("python", "/User/Desktop/python_ex.py");


        System.out.println("Process 시작");


        Process p2 = pb2.start();


        System.out.println("Process 종료");




        

    }

}

