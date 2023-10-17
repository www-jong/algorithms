# [Gold II] How Many Unicycles in a Wheel? - 17872 

[문제 링크](https://www.acmicpc.net/problem/17872) 

### 성능 요약

메모리: 33228 KB, 시간: 52 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2023년 8월 30일 15:27:56

### 문제 설명

<p>A Wheel Graph of size n is a cycle of n vertices each of which is connected to a center vertex. Examples of wheel graphs of size 4,5,6 and 8 are shown below:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 446px; height: 139px;"></p>

<p>A spanning unicycle in a graph, G, is a spanning tree in G with one additional edge added to form a single cycle. Each of the examples below is a spanning unicycle in a wheel graph of size 5:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 539px; height: 118px;"></p>

<p>Write a program to compute the number of different unicycles in a wheel graph of size n. Recall that two subgraphs, S1 and S2, of a graph G are different if there is at least one edge of G that is in S1 and not in S2 OR an edge in S2 which is not in S1.</p>

### 입력 

 <p>Input consists of a single line that contains a decimal integer, m (3 <= m <= 4000), which is the size of the wheel graph to find the number of unicycles of.</p>

### 출력 

 <p>The single output line consists of the count of unicycles modulo 100007 for the input size m.</p>

