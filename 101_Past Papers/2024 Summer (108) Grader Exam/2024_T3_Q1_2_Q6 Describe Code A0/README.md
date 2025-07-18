## Solution of 2024_T3_Q1 to Q6 ข้อ A0

Note : อาจารย์ตั้งใจให้เข้าใจพื้นฐานการทำงานของโค้ด จึงออกโจทย์ข้อ A0 ขึ้นมา เพื่อให้ได้ลองเขียนในการอธิบายโค้ดทั้งหมดออกมา (เขียนเป็น comment ไว้เหนือโค้ด) ด้านล่างนี้เป็นคำอธิบายของเเต่ละข้อ อยากให้สำหรับคนที่ไม่ค่อยเข้าใจได้ลองทำเองก่อน เเล้วค่อยมาเช็คเฉลยได้ว่าเข้าใจถูกมั้ย

### 2024_T3_Q1_A0 : Get Min-Max Out of 6 (1 Star)
- Input : รับค่า input เข้ามา 6 ตัวเเปร `d1 , d2 , d3 , d4 , d5 , d6`
- Process : ไล่เช็ค if ไปทีละค่า เพื่อหา `min (m1)` และ `max (m2)`
- Output : รวมค่า Sum จากสูตร `s = ทั้งหมด - min - max = (d1 + d2 + d3 + d4 + d5 + d6) - (m1 + m2)` แล้วส่งค่า s ออกมา
   
### 2024_T3_Q2_A0 : Interest Rate (1.5 Star)
- Input : รับค่า `principal (เงินต้น)` เพื่อจะคำนวณดอกเบี้ยทบต้น
- Process : เพิ่มอัตราดอกเบี้ยทบต้นด้วยสูตร `rate = r/12/100 โดย r เป็นเดือนที่ฝาก` ถ้าฝากเดือนที่ 1-4 จะได้ดอกเบี้ย 1% ต่อปี , ถ้าฝากเดือนที่ 5 หรือ 6 จะได้ดอกเบี้ย 2% , เดือนที่ 7 ได้ 3% ต่อปี , เดือนที่ 8 ได้ 4% ต่อปี , นานกว่านั้นจะได้ 7% ต่อปี
- Output : ทบค่าเข้าไปใน `total` แล้วเเสดงออกมา 2 ตำแหน่ง

### 2024_T3_Q3_A0 : Total Card Value (1.5 Star)
- Input : รับ C เข้ามาเป็น `string ของการ์ดเเต่ละใบ` จากนั้น `split` เป็น `list` เพื่อพิจารณาทีละ `element` ใน `list`
- Process : พิจารณาค่าของการ์ดเเต่ละใบ `(p)` ถ้าเป็นค่า 2,3,...,9 ให้มีค่าตามนั้น , ถ้าเป็น J,Q,K ให้มีค่า 10 , ถ้าเป็น Ace ให้มีค่าเป็น 1
- Output : รวมค่าเเต่ละใบลงตัวเเปร `total` จากนั้นเเสดงค่าออกมา

### 2024_T3_Q4_A0 : Average Grade (1.5 Star)
- Input : รับ G เข้ามาเป็น `string ของเกรดเเต่ละวิชา` จากนั้น `split` เป็น `list` เพื่อพิจารณาทีละ `element` ใน `list`
- Process : พิจารณาค่าของเกรดเเต่ละตัว `(g)` โดยพิจารณาเป็น Grade Letter ตามปกติ (ยกเว้น A+ เป็น 4 , A เป็น 3.75)
- Output : รวมค่าเเต่ละใบลงตัวเเปร `gx` จากนั้นเเสดงค่าออกมาเป็นทศนิยม 2 ตำแหน่ง

### 2024_T3_Q5_A0 : Move String Righthand (1 Star)
- Input : รับ string `s` เข้ามา และรับ `n` เป้นจำนวนตัวอักษรที่ต้องการเลื่อนออกไปทางขวา
- Process : ทำการวน loop และเพิ่ม `.` เข้าไปก่อนตัวอักษร โดยจะถูกทำให้ความยาวทั้งหมดเท่ากับตอนที่รับเข้ามา (เลื่อน string ไปทางขวาเรื่อยๆ)
- Output : แสดง `string s` ที่ถูกเลื่อนสตริงไป `n` ตำแหน่ง

### 2024_T3_Q6_A0 (อจ.บึ้ม Grader ไปก่อนละคับ YwY เสียใจด้วยๆ)
