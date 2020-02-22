import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    // Complete the compute_number_score function below.
    static int compute_number_score(int number) {
        return get_ans(number) + cons_five(number) + answer(number);
    }
    public static int get_ans(int num) {
        int s = 0;
        if (num % 3 == 0) s += 2;
        while (num > 0) {
            int d = num % 10;
            if (d == 7) s += 1;
            if (d % 2 == 0) s += 4;
            num = num / 10;
        }
        return s;
    }

    public static int cons_five(int num) {
        int s = 0;
        int cur_ones = 0;
        while (num > 0) {
            int d = num % 10;
            num = num / 10;
            if (d != 5 && cur_ones > 1) {
                s += 3;
                s += (cur_ones - 2) * 3;
                cur_ones = 0;
            }
            if (d != 5 && cur_ones == 1) {
                cur_ones = 0;
            }
            if (d == 5) {
                cur_ones++;
            }
        }
        if (cur_ones > 1) {
            s += 3;
            s += (cur_ones - 2) * 3;
        }
        return s;
    }

    public static int answer(int num) {
        int x = 0, count = 1;
        List < Integer > store = new ArrayList < > ();
        String s = Integer.toString(num);
        while (x < s.length() - 1) {
            if (s.charAt(x) == s.charAt(x + 1) + 1) {
                count++;
                x++;
            } else {
                x++;
                store.add(count);
                count = 1;
            }
        }
        store.add(count);
        int s = 0;
        for (Integer i: store) {
            s += i * i;
        }
        return s;
    }
    
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    // Complete the check_log_history function below.
    static int check_log_history(List<String> events) {
        HashSet<Integer> hs = new HashSet();
        Stack<Integer> s = new Stack();
        for(int i = 0; i < events.size(); i++){
            String t = events.get(i);
            String name = t.split(" ")[0];
            int number = Integer.parseInt(t.split(" ")[1]);
            if(name.equals("ACQUIRE")){
                if(hs.contains(number)){
                    return i+1;
                } 
                s.push(number);
                hs.add(number);
            }else{
                if(!hs.contains(number) || s.peek() != number){
                    return i+1;
                }
                s.pop();
                hs.remove(number);
            }     
        }
        return s.empty() ? 0 : events.size()+1;

    }