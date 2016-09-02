import java.util.Scanner;
import java.lang.Math;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int k=0;k<t;k++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

              //Main loop for each digit
            for(int i=0;i<n;i++){
            int sum=0;
            //calculating sum of 2's and adding with
                for(int j=0;j<=i;j++){
                sum+=Math.pow(2,j)*b;
                }
              sum+=a;
              System.out.printf("%d ",sum);
        }
               System.out.println();

        }
        in.close();
    }
}
