package graph;

import sun.security.util.BitArray;

import java.util.LinkedList;
import java.util.Queue;

public class Graph {
    private int v;
    private LinkedList<Integer>[] adj;

    public Graph(int v) {
        this.v = v;
        adj = new LinkedList[v];

        for (int i = 0; i < v; i++) {
            adj[i] = new LinkedList<>();
        }

    }

    public void addEdge(int s, int t) {
        adj[s].add(t);
        adj[t].add(s);
    }

    public void bfs(int s, int t) {
        if (s == t) return;
        boolean[] visited = new boolean[v];
        visited[s] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        int[] prev = new int[v];
        for (int i = 0; i < v; ++i) {
            prev[i] = -1;
        }

        while (queue.size() != 0) {
            int w = queue.poll();

            for (int q: this.adj[w]) {
                if (!visited[q]) {
                    prev[q] = w;
                    visited[q] = true;
                    if (q == t) {
                        this.printTrace(prev, s, t);
                        return;
                    }
                    queue.add(q);
                }
            }
        }

    }

    public void printTrace(int[] prev, int s, int t) {
        if (prev[t] != -1 && s != t) {
            printTrace(prev, s, prev[t]);
        }

        System.out.println(t);
    }

    public static void main(String[] args) {
        Graph graph = new Graph(8);
        graph.addEdge(0, 1);
        graph.addEdge(0, 3);
        graph.addEdge(1, 2);
        graph.addEdge(1, 4);
        graph.addEdge(2, 5);
        graph.addEdge(3, 4);
        graph.addEdge(4, 5);
        graph.addEdge(4, 6);
        graph.addEdge(6, 7);
        graph.addEdge(5, 7);

        graph.bfs(0, 7);
    }
}
