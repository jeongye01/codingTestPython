n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count+= n//coin#해당화폐로거슬러줄수있는동전의개수세기
    n %= coin
    
print(count)