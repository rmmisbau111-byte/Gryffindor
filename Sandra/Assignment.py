#creating a parity function to determine if a number is even or odd

def parity(num):
    if num% 2 == 0:
        return "even"
    else:
        return "odd"
    
num = int(input("Enter a number: "))
print(parity(num))    


#Using try and except function to pass an error.

def parity(num):

    if num% 2 == 0:
        return "even"
    else:
        return "odd"
    
while True:    
    try:
        user_input = int(input("Enter num: "))
        print(parity(user_input))
        break
    
    except(ValueError,TypeError):
        print("Invalid input") 
     


#Take a short video and divide it into its various picture frames

import cv2

video_path="C:\\Users\\user\\Desktop\\Gryffindor\\Sandra\\Vid.mp4"
output_folder="C:\\Users\\user\\Desktop\\Gryffindor\\Sandra\\Frames/"
cap=cv2.VideoCapture(video_path)
count=0

while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imwrite(f"{output_folder}frame_{count}.jpeg",frame)
    count+=1 

cap.release()


#Create a gif from a normal picture using pillow

from PIL import Image 
Img=Image.open("C:\\Users\\user\\Desktop\\Gryffindor\\Sandra\\GIFF.jpeg")

frames=[]

for i in range(5):
    size=(Img.width-i*10,Img.height-i*10)
    frame=Img.resize(size)
    frames.append(frame)

frames[0].save(
    "outpüt.gif",
    save_all=True,
    append_images=frames[1:],
    duration=500,
    loop=0
)

#search for the wildcards in python regex
import re

text = "cat bat rat mat caat ct color colour Python aaa aa aaaa"

print("Original Text:")
print(text)
print()

# 1. Dot wildcard .
pattern_dot = r".at"
matches_dot = re.findall(pattern_dot, text)
print("1. Dot wildcard (.) - matches any character before 'at'")
print("Pattern:", pattern_dot)
print("Matches:", matches_dot)
print()

# 2. Asterisk *
pattern_star = r"ca*t"
matches_star = re.findall(pattern_star, text)
print("2. Asterisk (*) - zero or more 'a'")
print("Pattern:", pattern_star)
print("Matches:", matches_star)
print()

# 3. Plus +
pattern_plus = r"ca+t"
matches_plus = re.findall(pattern_plus, text)
print("3. Plus (+) - one or more 'a'")
print("Pattern:", pattern_plus)
print("Matches:", matches_plus)
print()

# 4. Question mark ?
pattern_question = r"colou?r"
matches_question = re.findall(pattern_question, text)
print("4. Question mark (?) - optional 'u'")
print("Pattern:", pattern_question)
print("Matches:", matches_question)
print()

# 5. Square brackets []
pattern_brackets = r"[cb]at"
matches_brackets = re.findall(pattern_brackets, text)
print("5. Square brackets [] - match c or b before 'at'")
print("Pattern:", pattern_brackets)
print("Matches:", matches_brackets)
print()

# 6. Caret ^
pattern_caret = r"^cat"
matches_caret = re.findall(pattern_caret, text)
print("6. Caret (^) - match start of string")
print("Pattern:", pattern_caret)
print("Matches:", matches_caret)
print()

# 7. Dollar $
pattern_dollar = r"Python$"
matches_dollar = re.findall(pattern_dollar, text)
print("7. Dollar ($) - match end of string")
print("Pattern:", pattern_dollar)
print("Matches:", matches_dollar)
print()

# 8. Curly braces {}
pattern_braces = r"a{3}"
matches_braces = re.findall(pattern_braces, text)
print("8. Curly braces {} - exactly three 'a'")
print("Pattern:", pattern_braces)
print("Matches:", matches_braces)
print()