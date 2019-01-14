package alexnum;
import java.util.*;

/* Name of the class has to be "Main" only if the class is public. */
class ALEXNUM
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        while(t-- != 0)
        {
            long n=sc.nextLong();
            long ans = (n*(n-1))/2;
            System.out.print(ans+"\n");
            long temp;
            for(long i=0;i<n;i++)
                temp = sc.nextLong();
        }
    }
 }
