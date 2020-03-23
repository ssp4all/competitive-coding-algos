import java.util.*;
class Student{
    int roll;
    String name;
    Student(int roll, String name){
        this.roll = roll;
        this.name = name;
    }
}

class Main{
    public static void main(String[] args){
        // print("lool");
        List<Student> arr = new ArrayList<Student>();

        arr.add(new Student(0, "chutya"));
        arr.add(new Student(0, "ahutya"));
        
        Collections.sort(arr, new Comparator<Student>(){
                public int compare(Student a, Student b){
                    int x = a.roll - b.roll;
                    if (x == 0){
                        return a.name.compareTo(b.name);
                    }
                    return x; 
                }
            }
        );
        for (Student s: arr)
            System.out.println(s.roll + " " + s.name);
        // print(toString(arr));
    }

    static void print(String msg){
        System.out.println(msg);
    }
}