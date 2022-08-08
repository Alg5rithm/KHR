import java.util.*;

class Solution {
    public static ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
    public static boolean[] visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        for(int i=0; i<=n ;i++){
            list.add(new ArrayList<Integer>());
        }
        
        for(int i=0; i<computers.length; i++){
            for(int j=0; j<n; j++){
                if(computers[i][j] == 1 && i != j){
                    list.get(i+1).add(j+1);
                }
            }
        }
        visited = new boolean[n+1];
        for(int i=1; i<=n; i++){
            if(DFS(i) == true){
                answer += 1;
            }
        }
        return answer;
    }
    public static boolean DFS(int v){
        if(visited[v] == true){
            return false;
        }
        else{
            visited[v] = true;
            for(int i=0; i<list.get(v).size(); i++){
                DFS(list.get(v).get(i));
            }
            return true;
        }
    }
}
