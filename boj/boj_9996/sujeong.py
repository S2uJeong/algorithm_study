"""
1. 패턴에서 *의 위치를 알아낸다.
2. 슬라이싱을 통해 *의 앞 뒤 단어를 뽑아낸다.
3. 주어진 문자열에서 *의 앞쪽 문장이 있는지 확인 -> 없다면 false
4. 앞쪽 문장과 같은 글자까지를 끊은 뒤, 뒤 문장을 비교
"""
import sys
input = sys.stdin.readline

T = int(input())
pattern = input().rstrip()
star_idx = pattern.find('*')

sub1 = pattern[0:star_idx]
sub2 = pattern[star_idx + 1:]

for _ in range(T):
    input_string = input().rstrip()
    result1 = input_string[0:len(sub1)] == sub1
    result2 = input_string[-len(sub2):] == sub2

    if result1 and result2 and len(sub1) + len(sub2) <= len(input_string):
        print("DA")
    else:
        print("NE")
