import random

peta = [
        [1,2,3,4,5,],#r0
        [6,7,8,9,10],#r1
        [11,12,13,14,15],#r2
        [16,17,18,19,20],#r3
        [21,22,23,24,25],#r4
        ]

print(peta)
#set jumlah player
num_player = int(input("masukkan jumlah pemain: "))

#set posisi awal player
pos_player = []
for i in range(num_player):
    pos_player.append(peta[0][0])

print(pos_player)

ada_pemenang = False

while not ada_pemenang:
    #mengambil nilai dadu, dan menjalankan pemain sesuai langkah
    for i in range(num_player):
        langkah = random.randint(1, 6)
        pos_player[i] += langkah
        print(f"posisi player {i+1}: {pos_player[i]}")

        if pos_player[i] >= 25:
            print(f"selamat player{i+1} memenangkan permainan")
            ada_pemenang = True
            break
