# [Platinum III] Plug It In! - 16056 

[문제 링크](https://www.acmicpc.net/problem/16056) 

### 성능 요약

메모리: 187452 KB, 시간: 1120 ms

### 분류

이분 매칭

### 제출 일자

2025년 12월 4일 18:56:19

### 문제 설명

<p>Adam just moved into his new apartment and simply placed everything into it at random. This means in particular that he did not put any effort into placing his electronics in a way that each one can have its own electric socket.</p>

<p>Since the cables of his devices have limited reach, not every device can be plugged into every socket without moving it first. As he wants to use as many electronic devices as possible right away without moving stuff around, he now tries to figure out which device to plug into which socket. Luckily the previous owner left behind a plugbar which turns one electric socket into 3.</p>

<p>Can you help Adam figure out how many devices he can power in total?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line containing three integers m, n and k, where
	<ul>
		<li>m (1 ≤ m ≤ 1 500) is the number of sockets;</li>
		<li>n (1 ≤ n ≤ 1 500) is the number of electronic devices;</li>
		<li>k (0 ≤ k ≤ 75 000) is the number of possible connections from devices to sockets.</li>
	</ul>
	</li>
	<li>k lines each containing two integers x<sub>i</sub> and y<sub>i</sub> indicating that socket x<sub>i</sub> can be used to power device y<sub>i</sub>.</li>
</ul>

<p>Sockets as well as electronic devices are numbered starting from 1.</p>

<p>The plugbar has no cable, i.e. if it is plugged into a socket it simply triples it.</p>

### 출력 

 <p>Output one line containing the total number of electrical devices Adam can power.</p>

