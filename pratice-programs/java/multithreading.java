import java.util.*;
import java.io.*;

class Sender{
    void send(String msg){
        System.out.println("Sending..." + msg);
        try{
            Thread.sleep(1);
        }
        catch(Exception e){
            System.out.println("Thread interrupted..");
        }
    }
}
class Test extends Thread{
    private String s = "";
    Sender snd;
    Test(String msg, Sender obj){
        s = msg;
        snd = obj;
    }
    public void run(){
        synchronized(snd){
            snd.send(s);
        }
    }
}
class Main{
    public static void main(String[] args){
        System.out.println("WELCOME");
        Sender s = new Sender();
        Test t1 = new Test("HI", s);
        Test t2 = new Test("BYE", s);
        t1.start();
        t2.start();
        try{
            t1.join();
            t2.join();

        }
        catch (Exception e){
            System.out.println(e);
        }

        
    }
}