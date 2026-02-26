## Workshop 01_01 : Get Rectangle 
# Goal : รู้การสร้าง Object เเละ function เพิ่มเติมของ PyGame

# Step 1 : ตั้งค่าเริ่มต้นของ PyGame

# 1.1 import pygame + ตั้งค่า init 
import pygame as pg  # import library
pg.init()  # initialize pygame module

# 1.2 ตั้งค่า resolution ของ screen เเละ ตั้งค่าตัวเเปรเริ่มต้น
width = 540 #px 
height = 400 #px 
FPS = 60 #frame per second

# 1.3 ตั้งค่าตัวเเปรเริ่มต้น (speed object , ค่าสี RGB) 
speed = [2, 2] # 2 px per frame -> 120 px per sec

''' 
Note : อธิบายเรื่อง speed 
-> +2 ตัวเเรก คือ เคลื่อนที่ไปทาง +x (ไปทางขวา 2px/frame)
-> +2 ตัวหลัง คือ เคลื่อนที่ไปทาง -y (ลงด้านล่าง 2px/frame) !!ไม่เหมือนกับระบบพิกัดทั่วไป!! 
'''
black = (0, 0, 0) #R=0 , G=0 , B=0

# 1.4 นำเอาค่าในตัวแปร size ใช้ในการสร้าง screen resolution
screen = pg.display.set_mode((width,height))

# Step 2 : ส่วน main ของโปรเเกรม
# 2.1 : โหลดภาพจากภายนอกเข้ามาใช้ (ระวัง! 

### TO DO TASK #1 : copy path ของรูปลูกบอลที่เราต้องการ 

## Hint : อย่าลืมเปลี่ยน path ของรูปที่ใช้ จาก \ ให้เป็น / มิเช่นนั้นจะ error เพราะ track ที่มาของรูปไม่ได้)
    # โหลดภาพ ball มาจาก Path
ball = pg.image.load("C:/Users/Nine/CU Intania 108 (CP51) Programming All/2110101 Com Prog\Workshop CP 2024/Workshop 01 BNK Ball (PyGame)/Sources For Workshop #1/img/intro_ball.gif")
clock = pg.time.Clock() 
running = True

'''
ภาพ intro_ball ที่โหลดเข้ามาเก็บไว้ใน ball เป็นเพียง surface
การจะนำ surface มาใช้นั้นต้องเปลี่ยนให้เป็น object ที่มี attribute 
เนื่องจากรูปเป็นสี่เหลี่ยมเราจึงเลือกใช้ .get_rect() 
จะได้ object ที่มี height และ width เท่ากับภาพและมีจุดเริ่มต้นอยู่ที่บนซ้ายสุด 
(แต่ไม่มีภาพ มีแค่ attribute เหมือนเป็นกล่องสี่เหลี่ยนเปล่าวๆที่สามารถทำอะไรต่างๆได้)
ทำให้ทุกครั้งที่มีการเรียกใช้คำสั่ง pygame.image.load("...") มักจะใช้คำสั่ง .get_rect() ตามมาด้วย
'''
ballrect = ball.get_rect() # อย่าลืมเรียกคำสั่ง .get_rect() ด้วย

'''
รู้ไว้หน่อย! : attribute หลักๆของ object ที่ได้จาก .get_rect() 
เช่น .left   (ค่า x ซ้ายสุดสุดของ object) 
    .right  (ค่า x ขวาสุดของ object)
    .top    (ค่า y ด้านบนสุดของ object)
    .bottom (ค่า y ด้านล่างของ object)
'''

# 2.2 : เข้า while loop เพื่อเริ่มวงวนการทำงาน
while running:

    # 2.1 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม
    clock.tick(FPS) #ให้เเสดงผลด้วย FPS ตามที่เราตั้งไว้

    # 2.2 : วน loop การรับ event จาก mouse หรือ keyboard
    
    for event in pg.event.get():
        # 2.2.1 : ตรวจสอบว่า ถ้า event นั้นเป็นการคลิกปุ่มปิด x ให้ทำการปิดโปรแกรม
        
        if event.type == pg.QUIT: ## ผู้ใช้กดออก
            running = False
            pg.quit() # ออกจากเกม

    if running:
        # 2.2.2 : เนื่องจากเราแปลง ballrect กลายเป็น object แล้วเราสามารถให้มันขยับได้ด้วย คำสั่ง .move(...)
        ballrect = ballrect.move(speed)

        # 2.2.3 สร้าง condition ว่า ถ้า ball ทะลุกรอบซ้ายของจอ หรือ ทะลุกรอบขวาของจอให้กลับ
        if ballrect.left < 0 or ballrect.right > width: #px เลยกรอบซ้าย(px < 0) หรือ เลยขอบขวา (px > width)
            speed[0] = -speed[0] #กลับทิศความเร็วเเกน x
            
### TO DO TASK #2 (2.2.4) : จงทำให้บอลชิ่งไปมาในกรอบสี่เหลี่ยม (ไม่ตกกรอบ บน-ล่าง) [top , bottom] => ตอนนี้ทำได้เเค่ เด้งกลับ L-R
        
        # Hint : สร้าง condition คล้ายๆกับข้างบน 
        # โดย speed[0] หมายถึงแกน x และ speed[1] หมายถึงแกน y
        
        if ballrect.top < 0 or ballrect.bottom > height : #px เลยกรอบบน (px < 0) หรือ เลยขอบขวา (px > width)
            speed[1] = -speed[1]

        # 2.2.5 : ล้างทุกอย่างในจอโดยการให้จอเป็นสีดำ (ลอง comment code ดูสิจะเกิดอะไรขึ้น)
        screen.fill(black) # เติมให้สีจอเป้นดำ

        # 2.2.6 : เอาภาพ ball ใส่ใน object ballrect (ลอง comment code ดูสิว่าเกิดอะไรขึ้น)
        screen.blit(ball, ballrect) # รวม object เข้ากับภาพโดยใช้ .blit(element1 ,element2 , ...)

        # 2.2.7 : อัพเดท content ลงใน screen -> ในที่นี้คือการ นำเอา screen และ ballrect ใส่ลงใน window
        # (ลอง comment code ดูสิว่าเกิดอะไรขึ้น)
        
        pg.display.flip() # update content ลง screen
        
## Mod By Nine #1 General Gr.E เพื่อให้เข้าใจการทำงานมากขึ้น
