#include <iostream>

using namespace std;

const int MAX = 200005;
const int OFFSET = 100000;

int N;
int now = OFFSET;

int cnt_w[MAX]; // 흰색 칠한 횟수
int cnt_b[MAX]; // 검은색 칠한 횟수
int li[MAX];    // 0: 없음, 1: 흰색, 2: 검은색, 3: 회색

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    
    for (int j = 0; j < N; j++) {
        int a;
        char b;
        cin >> a >> b;

        if (b == 'L') {
            for (int i = 0; i < a; i++) {
                if (li[now] != 3) {
                    cnt_w[now]++;
                    if (cnt_w[now] >= 2 && cnt_b[now] >= 2) {
                        li[now] = 3;
                    } else {
                        li[now] = 1;
                    }
                }
                if (i < a - 1) now--; // 마지막 칸에서는 멈춤
            }
        } else {
            for (int i = 0; i < a; i++) {
                if (li[now] != 3) {
                    cnt_b[now]++;
                    if (cnt_w[now] >= 2 && cnt_b[now] >= 2) {
                        li[now] = 3;
                    } else {
                        li[now] = 2;
                    }
                }
                if (i < a - 1) now++; // 마지막 칸에서는 멈춤
            }
        }
    }

    int white = 0, black = 0, gray = 0;
    for (int i = 0; i < MAX; i++) {
        if (li[i] == 1) white++;
        else if (li[i] == 2) black++;
        else if (li[i] == 3) gray++;
    }

    cout << white << " " << black << " " << gray << "\n";
    return 0;
}