import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Main {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
       Main.reverseSpell(line);
    }
  }

  public static void reverseSpell(String str) {
    // Write your code here.
    String output="";
    for(int i=str.length()-1;i>=0;i--) {
      char x=str.charAt(i);
      if(Character.isDigit(x) || Character.isLetter(x)) {
	  	output=output+Character.toLowerCase(x)+"-";
      }
    }
    System.out.print(output.substring(0,output.length()-1)); 
  }
} 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.HashMap;

public class Main {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in);
    BufferedReader in = new BufferedReader(reader);

    try {
        double purchasePrice = Double.parseDouble(in.readLine());
        double cash = Double.parseDouble(in.readLine());
        Main.calculateChange(purchasePrice, cash);
    } catch (Exception e) {
        System.out.println(e);
    }
  }

  public static void calculateChange(double purchasePrice, double cash) {
    // Access your code here. Feel free to create other classes as required
        Map<Double,String> pounds=new HashMap();
		pounds.put(50.0, "Fifty Pounds");
		pounds.put(20.0, "Twenty Pounds");
		pounds.put(10.0, "Ten Pounds");
		pounds.put(5.0, "Five Pounds");
		pounds.put(2.0, "Two Pounds");
		pounds.put(1.0, "One Pound");
		Map<Double,String> pence=new HashMap();
		pence.put(50.0, "Fifty Pence");
		pence.put(20.0, "Twenty Pence");
		pence.put(10.0, "Ten Pence");
		pence.put(5.0, "Five Pence");
		pence.put(2.0, "Two Pence");
		pence.put(1.0, "One Pence");
		
		double difference=cash-purchasePrice;
        // DecimalFormat df2 = new DecimalFormat("#.##");
		// System.out.println(difference);
        if (difference < 0){
          System.out.print("ERROR");
          return ;
        }
        else if(difference == 0){
          System.out.print("Zero");
          return ;
        }
        
		double[] pound=new double[]{50.0,20.0,10.0,5.0,2.0,1.0};
		double[] pennies=new double[]{50.0,20.0,10.0,5.0,2.0,1.0};
		
		String output = "";
			//System.out.println(difference);
            while(difference>=1.00) {
              for(int i=0;i<pound.length;i++) {
                  if(difference>pound[i]) {
                      // System.out.print(pounds.get(pound[i]) +", ");
                      output += pounds.get(pound[i]) +", ";
                      difference-=pound[i];
                      break;
                  }
              }
            }
			difference *= 100;
          while(difference>=1.00) {
            for(int i=0;i<pennies.length;i++) {
              // System.out.print(difference);
                if(difference>=pennies[i]) {

                    // System.out.print(pence.get(pennies[i])+", ");
                  output += pence.get(pennies[i]) +", ";
                    difference-=pennies[i];
                  break;
                }
            }
           }
          System.out.print(output.substring(0, output.length()-2));
      }
}

import sys

def doSomething(blob, pattern):
    #print(blob, pattern)
    op = []
    add = 0
    l = len(blob)
    if not pattern:
        for i in range(l):
            op.append("0|")
        op.append("0")
        return "".join(op)
    
    ll = len(pattern)
    for i, value in enumerate(blob):
        temp = 0
        nn = len(value)
        for j in range(nn-ll+1):
            ss = value[j:j+ll]
            temp += ss.count(pattern)
        #c = value.count(pattern)
        op.append(str(temp)+"|")
        add += temp
        #print(op)
    return "".join(op+[str(add)])
       
    #return b
    #Write your code here
        
for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]
    blobs = splitted_input[1].split('|')
 
    result = doSomething(blobs, pattern)
    print(result)

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;

import java.util.List;
import java.util.stream.Collectors;


public class Main {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
      Main.matchBenchmark(line);
    }
  }
  
  public static void matchBenchmark(String ip) {
    // Access your code here. Feel free to create other classes as required
        
        
    String[] data=ip.split(":");
    String[] por=data[0].split("\\|");
    String[] bench=data[1].split("\\|");
    Map<String,Integer> dict=new HashMap();
    for(String x:por) {
        String[] actData=x.split(",");
        String check=actData[0]+","+actData[1];
        dict.put(check,Integer.parseInt(actData[2]));
    }
    for(String x:bench) {
        String[] actData=x.split(",");
        String check=actData[0]+","+actData[1];
        if(dict.containsKey(check)) {
            dict.put(check,dict.get(check)-Integer.parseInt(actData[2]));
        }
        else {
            dict.put(check,Integer.parseInt(actData[2])*-1);
        }
    }
    List<List> output=new ArrayList();
    for(String key:dict.keySet()) {
        String[] keySplit=key.split(",");
        if(dict.get(key)<0) {
            List list=new ArrayList(Arrays.asList("BUY",keySplit[0],keySplit[1],dict.get(key)*-1));
            output.add(list);
        }
        else if(dict.get(key)>0) {
            List list=new ArrayList(Arrays.asList("SELL",keySplit[0],keySplit[1],dict.get(key)));
            output.add(list);
        }
    }
    
    output = output.stream().sorted((o1,o2) -> {
        return ((String) o1.get(1)).compareTo((String) o2.get(1));
    }).collect(Collectors.toList());
    String prev = "";

    for (int i = 0; i<output.size();++i){
        List <String> temp = output.get(i);
        // System.out.println(temp.get(1));
        if((temp.get(1).compareTo(prev))==0){
            if (temp.get(2).compareTo("BOND") == 0){            
                Collections.swap(output, i-1, i);
            }
        }
        prev = temp.get(1);
    }

    for(List op:output) {
        System.out.println(op.get(0)+","+op.get(1)+","+op.get(2)+","+op.get(3));
    }
  }
}
/*
def matchBenchmark(input):
    if not input: return ""
    ip = input.split(":")
    por, bench = ip[0].split("|"), ip[1].split("|")
    cache = dict()
    n = len(por)
    for i in por:
        // Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15
        // Vodafone,STOCK,10|Google,STOCK,15:Vodafone,STOCK,15|Vodafone,BOND,10|Google,STOCK,10

        temp = i.split(",")      
        cache[(temp[0], temp[1])] = int(temp[2])
              
    for i in bench:
        temp = i.split(",")      
        if (temp[0], temp[1]) in cache:
            cache[(temp[0], temp[1])] -= int(temp[2])
        else:
            cache[(temp[0], temp[1])] = int(temp[2])*-1
    op = []
    for i in cache:
      if cache[i] < 0:
        op.append(["SELL", i[0], i[1], cache[i]*-1])
      elif cache[i] > 0:
        op.append(["BUY", i[0], i[1], cache[i]])
      else:
        pass
    op.sort(key=lambda x:(x[1], x[2]))
    for i in op:
        print(str(i[0])+", "+str(i[1])+", "+str(i[2])+", "str(i[3]))

*/
    
            

  