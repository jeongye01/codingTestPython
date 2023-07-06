//https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
////내 풀이->테스트 통과 DATE=>7.4 풀이시간 30분 
import java.util.Scanner;
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.HashSet;
import java.util.Set;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
		    int ans=1;
			int [][] arr=new int[9][9];
	    	for(int i=0;i<9;i++) {
	    		for(int j=0;j<9;j++) {
	    			arr[i][j]=sc.nextInt();
	    		}
	    	}
		    for(int i=0;i<9;i++) {
		        Set<Integer> hs=new HashSet<Integer>();
		        Set<Integer> hs2=new HashSet<Integer>();
		    	for(int j=0;j<9;j++) {
		    		hs.add(arr[i][j]);
		    		hs2.add(arr[j][i]);
		    	}
		    	if(hs.size()!=9 || hs2.size()!=9) {
		    		ans=0;
		    	}
		    }
		    if (ans==1) {
		    	for(int i=0;i<9;i+=3) {
			        
			    	for(int j=0;j<9;j+=3) {
                        Set<Integer> hs=new HashSet<Integer>();
			    		for(int k=0;k<3;k++) {
			    			for(int z=0;z<3;z++) {
			    				hs.add(arr[i+k][j+z]);
			    			}
			    		}
			    		if(hs.size()!=9) {
			    		ans=0;
			    	}
			    	}
			    	
			    }
		    }
		    System.out.println("#" +test_case+ " " + ans);

		}
	}
}