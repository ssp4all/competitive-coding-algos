import java.util.*;
class Student{
    int roll;
    String name, addr;

    public Student(int roll, String name, String addr){
        this.roll = roll;
        this.name = name;
        this.addr = addr;
    }

    public String toString(){
        return this.roll + " " + this.name + " " + this.addr;
    }
}

class sortByRoll implements Comparator<Student>{
    public int compare(Student a, Student b){
        return a.roll - b.roll;
    }
}

class Main{
    public static void helper(){
        TreeMap tm = new TreeMap(new sortByRoll());
        tm.put(new Student(19, "A", "B"), 2);
        tm.put(new Student(12, "C", "B"), 1);
        tm.put(new Student(13, "D", "B"), 3);

        System.out.print(tm);
    }
    public static void main(String[] args){
        
        helper();


        // System.out.println("Hello");
        // HashMap m = new HashMap();
        // HashSet s = new HashSet();
        // int a[] = {2,4,5,5,2};
        // List l = new ArrayList();
        // l.add(1);
        // l.add(1);
        // s.addAll(l);
        // System.out.print(s);
        // int a[] = {7,8,5,9,0};
        // System.out.print(a[0]);
        // List<String> list = new List<String>();
        // System.out.print(list);
        // ArrayList<String> al = new ArrayList();
        // // al.add("10");
        // al = {10, 20};
        // for(int i=0; i < al.size(); ++i){
        //     System.out.println(al[i]);
        // }
        // int[] a = {10, 20};
        // int n = a.len();
        // String x = Arrays.toString(a);
        // System.out.println(x);
        // Main m = new Main();
        // m.main();

        // for(int i:a){
        //     System.out.print(i);
        // }
        // Scanner sc = new Scanner();
        // sc.get()
    }
    // public void main(){
    //     System.out.println("Hello");
    //     int[] a = {10, 20};
    //     // int n = a.len();
    //     String x = Arrays.toString(a);
    //     System.out.println(x);
    //     // for(int i:a){
    //     //     System.out.print(i);
    //     // }
    //     // Scanner sc = new Scanner();
    //     // sc.get()
    // }

}
