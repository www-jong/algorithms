# [Platinum III] 호텔 관리 - 16915 

[문제 링크](https://www.acmicpc.net/problem/16915) 

### 성능 요약

메모리: 91256 KB, 시간: 1236 ms

### 분류

2-sat, 그래프 이론, 강한 연결 요소

### 제출 일자

2024년 7월 23일 14:51:50

### 문제 설명

<p>구사과 호텔에는 총 N개의 방이 있고, 방의 잠금 상태를 제어할 수 있는 스위치가 M개 있다. 모든 방은 두 개의 스위치와 연결되어 있다.</p>

<p>초기 방의 잠금 상태를 알고 있을 때, 스위치를 이용해 모든 방을 열려고 한다. 스위치를 누르면 연결된 방의 상태가 반전된다. 예를 들어, 방 1, 2, 3의 상태가 열림, 닫힘, 열림이고, 모두 스위치 1과 연결되어 있는 경우에 이 스위치를 누르면 방의 상태가 닫힘, 열림, 닫힘이 된다.</p>

<p>스위치를 이용해 모든 방을 열 수 있는지 알아보자.</p>

### 입력 

 <p>첫째 줄에 방의 개수 N(2 ≤ N ≤ 100,000)과 스위치의 개수 M(2 ≤ M ≤ 100,000)이 주어진다. 둘째 줄에는 초기 방의 잠금 상태가 1번 방부터 순서대로 주어진다. 0은 닫힌 상태, 1은 열린 상태이다.</p>

<p>셋째 줄부터 M개의 줄에는 스위치와 연결된 방의 정보가 주어진다. 각 스위치의 정보는 정수 K 하나와, K개의 공백으로 구분된 방 번호로 주어진다. 방 번호는 1 이상 N 이하의 정수이며, 주어지는 스위치들의 정보는 문제의 조건을 만족한다.</p>

### 출력 

 <p>모든 방을 열 수 있으면 1, 없으면 0을 출력한다.</p>

