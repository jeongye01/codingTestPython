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
	        int mx=-1;
	        int ans=0;
	        int[] points=new int[101];
	        for(int i=0;i<1000;i++) {
	        	int p=sc.nextInt();
	            points[p]+=1;
	        	
	        }
	        for(int i=0;i<=100;i++) {
	        	if (points[i]>=mx) {
	        		mx=points[i];
	        		ans=i;
	        	}
	        }
	    	
		    System.out.println("#" +tc+ " " + ans);
		    
	    }
	}
}