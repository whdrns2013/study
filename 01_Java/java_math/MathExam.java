import java.io.File;

import org.junit.Test;

public class MathExam{

    @Test
    public static void main(String[] args){

        //----파일 경로 선언----//
        String path = "C:\\Users\\USER\\Documents\\github_personal\\study\\Java\\java_math";
        
        //----파일 객체 생성----//
        File f = new File(path);

        //----폴더 내 객체 이름 반환----//
        String fileName = f.getName();
        System.out.println(fileName);

        //----폴더 객체 생성----//
        File folder = new File(path);

        //----폴더 내의 파일 리스트 반환----//
        File files[] = folder.listFiles();
        System.out.println("폴더에 포함된 파일 목록");
        for (int i=0; i < files.length; i++){
            File file = files[i];
            System.out.println(file);
        }

        //----파일의 부모 경로를 반환----//
        File file3 = new File(path + "exam.png");
        String parent = file3.getParent();
        System.out.println("부모 경로 : " + parent);

        //----파일의 parent, child를 이용해 경로 생성----//
        // File file4 = new File(path + "exam.png");
        // File parent2 = file4.getParent();
        // File files2[] = parent2.listFiles();
        // File filesFullPath[] = new File();
        // for (int i = 0; i < files2.length; i++){
            
        // }
        
        System.out.println("인덱싱");
        File newpath = new File("hi");
        files[0] = newpath;
        System.out.println(files[0]);

    }
}