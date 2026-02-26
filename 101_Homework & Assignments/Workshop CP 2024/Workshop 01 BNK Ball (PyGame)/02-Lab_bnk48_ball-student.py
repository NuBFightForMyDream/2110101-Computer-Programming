# Workshop 01_02 : Lab_BNK48 
# Goal : นำความรู้ที่เรียนมา (OOP , PyGame , While-If) มาลองสร้าง mini project ดู

# Step 1 : import pygame 
import pygame as pg

# Step 2 : ตั้งค่าเริ่มต้นของโปรเเกรม

## (2.1) TODO Task #1 : กำหนด width : 1000 , height : 600 และ FPS : 60
width = 1000 # px
height = 600 # px
FPS = 60 #frame per sec

## TODO Task #2 : กำหนดค่าสีดังนี้ pink : (197,142,195) , white : (255,255,255)
pink = (197 , 142 , 195)
white = (255 , 255 , 255)

# 2.2 : กำหนด ตป.เริ่มต้น ที่จำเป็นต้องใช้ขึ้นมา 

## TODO Task #3 : กำหนดความเร็วให้กับ member แต่ละคน ตามที่กำหนดให้ [3 member]
ball1_speed = [2,2]  # เลื่อนขวา +x 2 px/frame , เลื่อนลง -y 2 px/frame (120 px/sec) !! ระวัง ไม่ใช้พิกัด(x,y) เเต่ y จะเคลื่อนลงเสมอ (+)
ball2_speed = [-3,4] # เลื่อนซ้าย -x 3 px/frame , เลื่อนลง -y 4 px/frame (120 px/sec) 
ball3_speed = [3,-2] # เลื่อนขวา +x 3 px/frame , เลื่อนขึ้น +y 2 px/frame (120 px/sec)

## TODO Task #4 : สร้าง ตป.เริ่มต้น ของ pygame เเละสร้าง clock 
# (initialize pygame variable and create clock)

# 2.3 : ตั้งค่าเริ่มต้นของโปรเเกรม

pg.init() # ตั้งค่าเริ่มโปรเเกรม
clock = pg.time.Clock() # สร้าง ตป. clock
running = True #ตั้งค่าตัวเเปร running

## TODO Task #5 : สร้าง screen (width , height) ด้วยคำสั่ง pygame.display.set_mode เเละตั้งเเคปชั่น (ชื่อเเอป) เป็น "BNK_BALL (Heavy Collision)"
# (create screen [pygame.display.set_mode] and set caption [pygame.display.set_caption] => "BNK_BALL (Heavy Collision)")

screen = pg.display.set_mode((width,height))
caption = pg.display.set_caption('BNK_Ball (Heavy Collision)')

# 2.4 : สร้าง sound effect ที่ต้องใช้

## TODO Task #6 : โหลด sound จากภายนอก (จาก path ของ source ในเครื่องเรา) และเปลี่ยน path ด้วย
# (Load sound [change your sound filepath according to your computer])

# Hint : อย่าลืมเปลี่ยนข้างใน path จาก \ ให้เป็น / ด้วย (ใน windows) เพื่อให้โปรเเกรม track ได้
pg.mixer.init()
pg.mixer.music.load("C:/Users/Nine/CU Intania 108 (CP51) Programming All/Workshop CP 2024/Workshop 01_BNK Ball (PyGame)/Sources For Workshop #1/sound.mp3")
pg.mixer.music.play(-1, 0.0) # -1 = วน loop infinity , 0.0 คือ เริ่มเล่น sound effect ตอนเปิดเกม (ผ่านไปเเล้ว 0 วินาที)

# ใช้คำสั่ง soundeffect.play() เพื่อเล่นเสียง effect ตอนลูกบอลชนกัน
soundeffect = pg.mixer.Sound("C:/Users/Nine/CU Intania 108 (CP51) Programming All/Workshop CP 2024/Workshop 01_BNK Ball (PyGame)/Sources For Workshop #1/effect.wav")

# 2.5 : import รูป idol BNK48 มา 3 คน เพื่อสร้าง element เกี่ยวกับรูปภาพ

# TODO Task #7 : create object with attribute in each comment

# Choose 3 members from BNK48 and create pygame object from  get_rect => [ load , resize , get_rect ]

# Note : อย่าลืมเปลี่ยน path จาก \ ให้เป็น / ด้วย

# Member 1 [size : (150 , 150) , center : (500 , 250) ] => Wee
ball1_img = pg.image.load("C:/Users/Nine/CU Intania 108 (CP51) Programming All\Workshop CP 2024/Workshop 01_BNK Ball (PyGame)/Sources For Workshop #1/BNK48/Wee_cc.png").convert_alpha() #load
ball1_img = pg.transform.scale(ball1_img, (150, 150)) #resize
ball1_rect = ball1_img.get_rect(center=(500,250)) #get_rect

# Member 2 [size : (100 , 100) , center : (250 , 120)] => Cherprang
ball2_img = pg.image.load("C:/Users/Nine/CU Intania 108 (CP51) Programming All/Workshop CP 2024/Workshop 01_BNK Ball (PyGame)/Sources For Workshop #1/BNK48/Cherprang_cc.png").convert_alpha() #load
ball2_img = pg.transform.scale(ball2_img , (100,100)) #resize
ball2_rect = ball2_img.get_rect(center=(250,120)) #get_rect

# Member 3 [size : (120 , 120) , center : (800 , 400)] => Bamboo
ball3_img = pg.image.load("C:/Users/Nine/CU Intania 108 (CP51) Programming All/Workshop CP 2024/Workshop 01_BNK Ball (PyGame)/Sources For Workshop #1/BNK48/Bamboo_cc.png").convert_alpha() #load
ball3_img = pg.transform.scale(ball3_img , (120,120)) #resize
ball3_rect = ball3_img.get_rect(center=(800,400)) #get_rect

# Step 3 : ส่วน main ของโปรเเกรม => สร้างเงื่อนไขของ object & การชน

while running:
    # TODO Task #8 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม [clock.tick(...)]
    clock.tick(FPS) # กำหนดความเร็วให้เท่ากับ FPS (ที่กำหนดไว้ด้านบน)

    for event in pg.event.get(): # pg.event.get() คือ ดูว่าผู้ใช้รับ input อยู่มั้ย?
        if event.type == pg.QUIT: # user กดออก
            running = False # หยุดทำงาน
            pg.quit() # สั่งปิดโปรเเกรม

    if running:
        # TODO Task #9 :ใส่สี background สีชมพู (screen.fill(...))
        screen.fill(pink)

        # TODO Task #10 : ให้ member ทั้ง 3 คนเคลื่อนที่ตามทิศทางและความเร็วเป็นไปตาม speed ของแต่ละคน (ให้ object เคลื่อนที่)
        ball1_rect = ball1_rect.move(ball1_speed)
        ball2_rect = ball2_rect.move(ball2_speed)
        ball3_rect = ball3_rect.move(ball3_speed)
        
        # TODO Task #11 : วาด text คำว่า "Heavy Collision" [size : 150 , center :(width/2 , height/3), สีขาว] (ดูจากไฟล์ & doc ได้)
        font_name = pg.font.match_font('arial')                         # กำหนดชื่อ Font
        font = pg.font.Font(font_name, 150)                             # กำหนดขนาด font
        text_surface = font.render("Heavy Collision", True, white)      # กำหนด Text เเละสี
        text_rect = text_surface.get_rect()                             # แปลง Surface เป็น object 
        text_rect.midtop = (width/2 , height/3)                         # ระบุตำเเหน่งของ text 
        screen.blit(text_surface, text_rect)                            # เอา Text ใส่ลงใน object ของ Text นั้น

        
        # TODO Task #12 : วาด text รหัสนิสิต ลงไป ข้างใต้คำว่า "Heavy Collision" [size : 100 ,center :(width/2 , height/1.5), สีขาว]
        # [ขนาดและตำแหน่งสามารถปรับได้ตามความเหมาะสม]
        font = pg.font.Font(font_name, 100)                                 # กำหนดขนาด font
        text_surface = font.render("6730084521 Chatrphol", True, white)     # กำหนด Text เเละสี
        text_rect = text_surface.get_rect()                                 # แปลง Surface เป็น object 
        text_rect.midtop = (width/2 , height/1.5)                           # ระบุตำเเหน่งของ text 
        screen.blit(text_surface, text_rect)                                # เอา Text ใส่ลงใน object ของ Text นั้น

        # TODO 13 : เขียนเงื่อนไขไม่ให้ตกกรอบทุกด้านให้กับ member ทั้ง 3 คน
        
        # Ball #1 (Wee) => check เงื่อนไข ซ้าย-ขวา & บน-ล่าง
        
        if ball1_rect.left < 0 or ball1_rect.right > width: # #px เลยกรอบซ้าย(px < 0) หรือ เลยขอบขวา (px > width)
            ball1_speed[0] = -ball1_speed[0] # กลับทิศความเร็วเเกน x 
            
        if ball1_rect.top < 0 or ball1_rect.bottom > height: # px เลยกรอบบน (px < 0) หรือ เลยขอบขวา (px > width)
            ball1_speed[1] = -ball1_speed[1] # กลับทิศความเร็วเเกน y

        # Ball #2 (Cherprang) => check เงื่อนไข ซ้าย-ขวา & บน-ล่าง
        
        if ball2_rect.left < 0 or ball2_rect.right > width: # #px เลยกรอบซ้าย(px < 0) หรือ เลยขอบขวา (px > width)
            ball2_speed[0] = -ball2_speed[0] # กลับทิศความเร็วเเกน x 
            
        if ball2_rect.top < 0 or ball2_rect.bottom > height: # px เลยกรอบบน (px < 0) หรือ เลยขอบขวา (px > width)
            ball2_speed[1] = -ball2_speed[1] # กลับทิศความเร็วเเกน y
            
        # Ball #3 (Bamboo) => check เงื่อนไข ซ้าย-ขวา & บน-ล่าง
        
        if ball3_rect.left < 0 or ball3_rect.right > width: # #px เลยกรอบซ้าย(px < 0) หรือ เลยขอบขวา (px > width)
            ball3_speed[0] = -ball3_speed[0] # กลับทิศความเร็วเเกน x 
            
        if ball3_rect.top < 0 or ball3_rect.bottom > height: # px เลยกรอบบน (px < 0) หรือ เลยขอบขวา (px > width)
            ball3_speed[1] = -ball3_speed[1] # กลับทิศความเร็วเเกน y        

        # TODO 14 : Special point ทำให้ลูกบอลชนกันแล้วเด้งในทิศตรงกันข้าม
        
        # Logic : รัศมี 2 ลูกรวมกัน > ระยะห่างระหว่าง 2 ลูก
        
        # ใช้ คำสั่ง .collidirect เเล้วเล่น sound effect ขณะชนกัน (มันจะดูเฟคๆนิดหน่อย เเต่ไม่เป็นไร)
        
        if ball1_rect.colliderect(ball2_rect):
            ball1_speed[0], ball2_speed[0] = -ball1_speed[0], -ball2_speed[0] # กลับทิศเเกน x
            ball1_speed[1], ball2_speed[1] = -ball1_speed[1], -ball2_speed[1] # กลับทิศเเกน y
            soundeffect.play()

        if ball1_rect.colliderect(ball3_rect):
            ball1_speed[0], ball3_speed[0] = -ball1_speed[0], -ball3_speed[0] # กลับทิศเเกน x
            ball1_speed[1], ball3_speed[1] = -ball1_speed[1], -ball3_speed[1] # กลับทิศเเกน y
            soundeffect.play()

        if ball2_rect.colliderect(ball3_rect):
            ball2_speed[0], ball3_speed[0] = -ball2_speed[0], -ball3_speed[0] # กลับทิศเเกน x
            ball2_speed[1], ball3_speed[1] = -ball2_speed[1], -ball3_speed[1] # กลับทิศเเกน y
            soundeffect.play()

        # TODO 15 : เอาภาพของ member แต่ละคนใส่ลงใน object ของตนเอง
        screen.blit(ball1_img, ball1_rect)
        screen.blit(ball2_img, ball2_rect)
        screen.blit(ball3_img, ball3_rect)

        # Final : ทำการอัพเดท screen 
        pg.display.flip()