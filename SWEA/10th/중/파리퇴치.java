//https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
//내 풀이->테스트 통과 DATE=>7.4 풀이시간 40분 
import java.util.Scanner;
import java.io.FileInputStream;
 
class Solution
{
    public static void main(String args[]) throws Exception
    {
 
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
           for(int tc=1;tc<=T;tc++) {
            int ans=0;
            int n=sc.nextInt();
            int m=sc.nextInt();
            int [][] arr=new int[n+(m-1)*2][n+(m-1)*2];
            for(int i=m-1;i<n+m-1;i++) {
                for(int j=m-1;j<n+m-1;j++) {
                    arr[i][j]=sc.nextInt();
                }
            }
            for(int i=m-1;i<n+m-1;i++) {
                for(int j=m-1;j<n+m-1;j++) {
                    int tmp1=arr[i][j]*-1;
                    int tmp2=arr[i][j]*-3;
                    for(int k=(m-1)*-1;k<=m-1;k++) {
                        tmp1+=arr[i][j+k];
                        tmp1+=arr[i+k][j];
                         
                    }
                    for(int k=0;k<=m-1;k++) {
                        tmp2+=arr[i+k][j+k];
                        tmp2+=arr[i-k][j-k];
                        tmp2+=arr[i+k][j-k];
                        tmp2+=arr[i-k][j+k];
                         
                    }
                    ans=Math.max(Math.max(tmp1, tmp2),ans);
                     
                }
            }
             
            System.out.println("#" +tc+ " " + ans);
        }
         
    }
}