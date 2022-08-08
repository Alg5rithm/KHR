import java.util.*;
class Solution {
    public final static int INF = (int) 1e9;
    public static int[] d;
    public ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    public int solution(int n, int[][] edge) {
        int answer = 0;
        for(int i=0; i<=n; i++){
            graph.add(new ArrayList<Node>());
        }
        for(int i=0; i<edge.length; i++){
            int x = edge[i][0];
            int y = edge[i][1];
            graph.get(x).add(new Node(y, 1));
            graph.get(y).add(new Node(x, 1));
        }
        
        
        d = new int[n+1];
        Arrays.fill(d, INF);
        int start = 1;
        dijkstra(start);
        int max = 0;
        for(int i=1; i<=n; i++){
            if(max < d[i]){
                max = d[i];
            }
        }
        
        for(int i=1; i<=n; i++){
            if(max == d[i]) answer += 1;
        }
        
        return answer;
    }
    
    public void dijkstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));
        d[start] = 0;
        
        while(!pq.isEmpty()){
            Node node = pq.poll();
            int dist = node.getDistance();
            int now = node.getIndex();
            
            if(d[now] < dist) continue;
            
            for(int i=0; i<graph.get(now).size(); i++){
                int cost = graph.get(now).get(i).getDistance() + dist;
                if(cost < d[graph.get(now).get(i).getIndex()]){
                    d[graph.get(now).get(i).getIndex()] = cost;
                    pq.add(new Node(graph.get(now).get(i).getIndex(), cost));
                }
            }
        }
    }
    
}

class Node implements Comparable<Node>{
    private int index;
    private int distance;
    
    public Node(int index, int distance){
        this.index = index;
        this.distance = distance;
    }
    
    public int getIndex(){
        return this.index;
    }
    
    public int getDistance(){
        return this.distance;
    }
    
    @Override
    public int compareTo(Node other){
        if(this.distance < other.distance){
            return -1;
        }
        return 1;
    }
}
