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