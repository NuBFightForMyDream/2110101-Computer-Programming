# create word check (repeat) = pattern x 2
# logic : check if word range = repeat
    # if yes count++ & add pos with len(pattern)
    # else add pos 1
    
def get_repeat_count(data , pattern) :
    count = 0
    i = 0
    repeat = pattern * 2 # ต้องเจออย่างน้อย 2 ครั้งติดกัน
    
    while i <= len(data) - len(repeat):
        if data[i:i+len(repeat)] == repeat:
            count += 1
            i += len(pattern)  # ขยับทีละ 1 pattern เพื่อหาติดกันหลายรอบ
        else:
            i += 1
            
    return count


# รับข้อมูล
pattern = input().strip()
n = int(input().strip())

for _ in range(n):
    data = input().strip()
    print(get_repeat_count(data, pattern))