### Workshop 1 : Pygame

# Goal : ต้องการสร้าง BNK Ball (ลูกบอล 3 ลูก เด้ง & ชนกันไปเรื่อยๆ)

# Key :
# 1. เข้าใจการทำงานของ while , for , if-else
# 2. เข้าใจ Overview ของ Object-Oriented Programming
# 3. รู้วิธีการสร้าง object เเละ การเรียกใช้ method ใน pygame

# Step :
# 01_00 : Pygame Starter => รู้ fn พื้นฐาน เพื่อใช้ในกาารทำ BNK Ball [มี Task ให้เเก้ไขโค้ดเล็กน้อย]
# 01_01 : Get Rectangle => สร้าง object (ซึ่งก็คือ สี่เหลี่ยมผืนผ้า เพื่อใช้ในการสร้างการเด้งลูกบอล) [มี Task ให้เเก้ไขโค้ดเล็กน้อย]
# 01_Final : BNK Ball => นำความรู้จาก 01_00 เเละ 01_01 มาทำการสร้าง BNK Ball ออกมา [เเก้ไขโค้ดทั้งชิ้นงาน]

# Step 1 : ทำการ import library ที่ต้องใช้งาน (ซึ่งคือ pygame) โดยเราจะตั้งชื่อย่อในนาม pg (เพื่อสะดวกในการเขียน)
import pygame as pg

# Step 2 : ทำการตั้งค่าเริ่มต้นของเกม

# 2.1 : ส่วน UI ของเกม

    # 2.1.1 คำสั่งเริ่มต้นเกม
pg.init() # เพื่อเริ่มค่า pygame modules

    # 2.1.2 ตั้งค่าสีที่จำเป็นต้องใช้ (ใน format (R,G,B) )
black = (0,0,0)
white = (255,255,255)
green = (193,225,193)
red = (255,87,51)
pink = (255,209,220)
purple = (195,177,225)

    # 2.1.3 ตั้งค่าหน้าตาเกม
width = 700     # กว้าง 700 px
height = 500    # ยาว 500 px
FPS = 60        # เเสดงผล 60 frame ต่อวินาที

    # 2.1.4 เเสดงผลหน้าจอเกม
screen = pg.display.set_mode((width,height)) # กำหนดขนาดหน้าจอ
pg.display.set_caption("Workshop 01_00 Pygame Starter ECN_CP") # เเสดงเเคปชั่น (ชื่อเเอพ) ขึ้นบนจอ จะอยู่บนหัวเเอป)
clock = pg.time.Clock() # สร้าง ตป. clockขึ้นมา (คิดว่าน่าจะเพื่อเเสดงผล กก.FPS)


# TASK TO DO #1 : Define Running => เราจะสร้าง ตป. running โดยให้ค่าเป็น True (สั้นๆคือ while True เเม่งไม่สวย ;w;)
# running =  ตป.ที่ให้ค่าว่า โปรเเกรมเกมกำลังรันอยู่?

### ใส่คำสั่งด้านล่างนี้ 
running = True
### ???


# Step 3 : เข้าสู่ main ของเกม => สร้าง loop เพื่อเช็คว่า โปรเเกรมกำลังรันอยู่มั้ย? 

# TASK TO DO #2 : เปลี่ยน Boolean ให้เป็น ตัวเเปร ใน while loop 

while running : 
    # 3.1 ตั้งค่าให้เกมเเสดงผลตาม FPS ที่กำหนด
    clock.tick(FPS)
    
    # 3.2 สร้าง for loop เพื่อรับ input จากภายนอก (เมาส์/คียบอร์ด)
    for event in pg.event.get():
        if event.type == pg.QUIT: # ตรวจสอบว่า user ต้องการปิดโปรเเกรมมั้ย?
            
            # TO DO TASK #3 : สั่งให้โปรเเกรมหยุดทำงาน 
            # ???
            pg.quit()
    
# Step 4 : สร้างองค์ปรพกอบที่เหลือในเกม

    # 4.1 background color 
    screen.fill(pink) #เติมสี background ให้เป็นสี pink (เรา define RGB ของ pink ไว้ก่อนหน้าเเล้ว)
    
    # 4.2 draw text เป็นเลขรหัสนิสิต 10 หลัก [กำหนดให้ size : 80 และ center อยู่ที่ (width/2 , height/4)] (กลับไปเช็คว่า width และ height คืออะไร)
    ## จากที่เช็คมา width เเละ height คือขนาดหน้าตาเกม
    
        # 4.2.1 ตั้งชื่อ font ฿ คุณสมบัติ ของ text ที่เราจะวาด
    font_name = pg.font.match_font('arial') # กำหนดชื่อ Font 
    font = pg.font.Font(font_name, 80) # กำหนดขนาด font (80 px)
    text_surface = font.render("6730084521", True, black) # กำหนด Text (เลขนิสิต) และ สี (ดำ)    
       
        # 4.2.2 ทำการเปลี่ยนชนิด จาก surface ให้เป็น object (เนื่องจากเป็นการเขียน OOP -> )
    
    text_rect = text_surface.get_rect() # แปลง Surface เป็น object
    text_rect.midtop = (400, 300) # ระบุตำแหน่งของ text
    screen.blit(text_surface, text_rect) # เอา Text ใส่ลงใน object ของ Text นั้น (ใช้คำสั่ง blit)

        # 4.2.3 สร้าง element อื่นๆขึ้นมา เช่น สี่เหลี่ยมผืนผ้า (rectangle) , เส้นตรง (line) , วงรี (eclipse)
        
        # วาด บน screen ที่เรา set ไว้ , โดย [x, y, width, height] , ความหนาเส้นรอบวง
    pg.draw.rect(screen, red,[55,200,100,70],0) 
    pg.draw.line(screen, green ,[20,35],[250,160],5)
    pg.draw.ellipse(screen , black , [340,100,250,100], 2)
    # More about draw : https://www.pygame.org/docs/ref/draw.html

    # ให้เเสดงผลภาพที่เราวาดทันที
    pg.display.flip()

## Mod By Nine #1 General Gr.E เพื่อให้เข้าใจการทำงานมากขึ้น