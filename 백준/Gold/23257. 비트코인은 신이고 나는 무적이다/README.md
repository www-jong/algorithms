# [Gold III] 비트코인은 신이고 나는 무적이다 - 23257 

[문제 링크](https://www.acmicpc.net/problem/23257) 

### 성능 요약

메모리: 31256 KB, 시간: 1064 ms

### 분류

다이나믹 프로그래밍, 배낭 문제

### 제출 일자

2023년 9월 24일 18:58:09

### 문제 설명

<p>코인 경력 4년차, 차트에 통달한 찬호는 이전 $N$개의 월봉을 통해 다음 월봉의 절댓값을 예측할 수 있는 아래의 공식을 만들어냈다.</p>

<p style="text-align: center;">(다음 월봉의 절댓값) = 이전 $N$개의 월봉 중 중복을 허용해 $M$개를 골라 절댓값들을 <a href="https://ko.wikipedia.org/wiki/%EB%B9%84%ED%8A%B8_%EC%97%B0%EC%82%B0">bitwise xor</a> 한 것 중 최대</p>

<p>$N$, $M$, 이전 월봉들 $A_i$들이 주어졌을 때 다음 월봉의 절댓값을 구해보자.</p>

### 입력 

 <p>첫째 줄에 $N$, $M$이 주어진다.</p>

<p>둘째 줄에 $A_1, A_2, \cdots , A_N$이 주어진다.</p>

### 출력 

 <p>다음 월봉의 절댓값을 출력하라.</p>

