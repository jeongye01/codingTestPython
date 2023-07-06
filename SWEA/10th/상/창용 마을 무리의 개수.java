//https://ongveloper.tistory.com/483

//dfs
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {

	static int n,m;
	static int[] input;
	static boolean[] visited;
	static ArrayList<Integer>[] edge;
	
	static void dfs(int cur) {
		visited[cur] = true;
		
		for(int next : edge[cur]) {
			if(visited[next]) continue;
			dfs(next);
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
		int T = Integer.parseInt(br.readLine());
		for(int t=1; t<=T; t++) {
			//input
			int answer=0;
			StringTokenizer tk = new StringTokenizer(br.readLine());
			n = Integer.parseInt(tk.nextToken());
			m = Integer.parseInt(tk.nextToken());
			input = new int[n+1]; 
			visited = new boolean[n+1];
			edge = new ArrayList[n+1];
			for(int i=1; i<= n; i++) {
				edge[i] = new ArrayList<Integer>();
			}
			for(int i=0; i<m; i++) {
				int from,to;
				tk = new StringTokenizer(br.readLine());
				from = Integer.parseInt(tk.nextToken());
				to = Integer.parseInt(tk.nextToken());
				edge[from].add(to);
				edge[to].add(from);
			}
			
			//solve
			for(int i=1; i<=n; i++) {
				if(visited[i]) continue;
				dfs(i);
				answer++;
			}
			
			//output
			bw.write("#" + t+ " " + answer +'\n');
		}
		bw.close();	
	}
}

//union-find
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
	 
    static int n,m;
    static int[] parent;

    static int getParent(int x) {
    	if (parent[x]==x) return x;
    	else return parent[x] = getParent(parent[x]);
    }
    
    static void unionParent(int x, int y) {
      x = getParent(x);
      y = getParent(y);
      
      if(x<y) 
    	  parent[y]=x;
      else 
    	  parent[x]=y;
    }
     
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
     
        int T = Integer.parseInt(br.readLine());
        for(int t=1; t<=T; t++) {
            //input
            int answer=0;
            StringTokenizer tk = new StringTokenizer(br.readLine());
            n = Integer.parseInt(tk.nextToken());
            m = Integer.parseInt(tk.nextToken());
            parent = new int[n+1];
            for(int i=1; i<=n; i++) {
            	parent[i] = i;
            }
            
          //solve
            for(int i=0; i<m; i++) {    
                tk = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(tk.nextToken());
                int to = Integer.parseInt(tk.nextToken());
                unionParent(from,to);
            }
             
            //부모 값이 자기 자신과 같은 것의 개수가 그룹의 개수
            for(int i=1; i<=n;i++) {
            	if(parent[i]==i) {
            		answer++;
            	}
            }
             
            //output
            bw.write("#" + t+ " " + answer +'\n');
        }
        bw.close(); 
    }
}