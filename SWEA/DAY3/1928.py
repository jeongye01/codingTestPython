#Base64 Decoder
#내 풀이 아님
base_list = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
base_list.extend([chr(x) for x in range(ord('a'), ord('z') + 1)])
base_list.extend([chr(x) for x in range(ord('0'), ord('9') + 1)])
base_list.append('+')
base_list.append('/')
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    buffer = input()
    tmp = [bin(base_list.index(s))[2:].zfill(6) for s in buffer]
    tmp = "".join(tmp)
    out = ""
    for i in range(0, len(tmp), 8):
        out += chr(int(tmp[i:i+8], 2))
    print(f"#{test_case}", out)  