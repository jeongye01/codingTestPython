//https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
////내 풀이->테스트 통과 DATE=>7.4 풀이시간 15분 
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
	        int n=sc.nextInt();
	        int m=sc.nextInt();
	        int ans=-1*(10^9);
	        int[] a=new int[n];
	        int[] b=new int[m];
	    	for(int i=0;i<n;i++) {
	    		a[i]=sc.nextInt();
	    		
	    	}
	    	for(int i=0;i<m;i++) {
	    		b[i]=sc.nextInt();
	    		
	    	}
	    	if(n<m) {
	    		for(int i=0;i<=m-n;i++) {
	    			int tmp=0;
	    			for(int j=0;j<n;j++) {
	    				tmp+=b[i+j]*a[j];
	    			}
	    			ans=Math.max(tmp,ans);
	    			
	    		}
	    		
	    	}else {
	    		for(int i=0;i<=n-m;i++) {
	    			int tmp=0;
	    			for(int j=0;j<m;j++) {
	    				tmp+=a[i+j]*b[j];
	    			}
	    			ans=Math.max(tmp,ans);
	    			
	    		}
	    	}
	    	
	    	
		    System.out.println("#" +tc+ " " + ans);
		    
		   
		   
		   
	       
	    }
	}
}