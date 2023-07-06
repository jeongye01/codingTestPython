//https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
////내 풀이->테스트 통과 DATE=>7.4 풀이시간 60분 
//https://yongku.tistory.com/entry/SW-expert-Academy-SWEA-1961%EB%B2%88-%EC%88%AB%EC%9E%90-%EB%B0%B0%EC%97%B4-%ED%9A%8C%EC%A0%84-%EC%9E%90%EB%B0%94Java
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
	    	int [][] arr=new int[n][n];
	    	for(int i=0;i<n;i++) {
	    		for(int j=0;j<n;j++) {
	    			arr[i][j]=sc.nextInt();
	    		}
	    	}
	    	String [][] turn_arr=new String[n][3];
	    	for(int i=0;i<3;i++) {
		    	for(int y=0;y<n;y++) {
		    		
		    			turn_arr[y][i]="";
		    			
		    		
		    	}
	    	}
	        
		    for(int i=0;i<3;i++) {
		    	int[][] rotate = new int[n][n];
		    	for(int y=0;y<n;y++) {
		    		for(int x=0;x<n;x++) {
		    			rotate[y][x]=arr[n-1-x][y];
		    			
		    		}
		    	}
		    	arr=rotate.clone();
		    	for(int y=0;y<n;y++) {
		    		for(int x=0;x<n;x++) {
		    			turn_arr[y][i]+=rotate[y][x];
		    		}
		    	}
		    	
		    }
		    System.out.println("#" +tc);
		    
		    for(int y=0;y<n;y++) {
		    	for(int i=0;i<3;i++) {
		    		System.out.print(turn_arr[y][i]+" ");
		    		
		    	}
		    	System.out.println();
		    	
		    }
		   
		   
	       
	    }
	   
	}
}