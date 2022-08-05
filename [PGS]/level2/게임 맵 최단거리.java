import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length; 
        int m = maps[0].length; 
        boolean[][] visited = new boolean[n][m];
        
        answer = BFS(n, m, maps, visited);
        
        if (answer == 1){
            return -1;
        }
        return answer;
    }
    
    public int BFS(int n, int m, int[][] maps, boolean[][] visited){
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[2]);
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        while (!queue.isEmpty()){
            int[] temp = queue.poll();
            int x = temp[0];
            int y = temp[1];
            visited[x][y] = true;
            for(int i = 0 ; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (maps[nx][ny] == 0) continue;
                if (maps[nx][ny] == 1 && !visited[nx][ny]){
                    maps[nx][ny] = maps[x][y] + 1;
                    int[] newXY = {nx, ny};
                    queue.add(newXY);
                }
            }
        }
        return maps[n-1][m-1];
        
    }
}
