package com;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class StackBOJ {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Deque<Integer> deque = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++){
            String input = br.readLine();
            String[ ] str = input.split(" ");
            String order = str[0];
            
            switch (order) {
                case "top":
                    if (deque.isEmpty()){
                        sb.append(-1+"\n");
                    } else {
                        sb.append(deque.peek()+"\n");
                    }
                    break;
                case "size":
                        sb.append(deque.size()+"\n");
                    break;
                case "empty":
                    if (deque.isEmpty()){
                        sb.append(1+"\n");
                    } else {
                        sb.append(0+"\n");
                    }
                    break;
                case "pop":
                    if (deque.isEmpty()){
                        sb.append(-1+"\n");
                    } else {
                        sb.append(deque.pop()+"\n");
                    }
                    break;
                case "push":
                    int val = Integer.parseInt(str[1]);
                    deque.push(val);
                    break;
                default:
                    break;
                }

        }
        br.close();
        System.out.print(sb);
    }
}
