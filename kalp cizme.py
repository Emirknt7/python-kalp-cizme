                                             # python ile kalp çizdirme
import turtle  # turtle kütüphanesi ekleme
kalem=turtle.Turtle() # kalem adından bir turtle nesnesi oluşturma
kalem.up() # up kalemin cizme işlemini durdur
kalem.goto(0,-200) # goto istenilen kordinatlara gitmeye yarar
kalem.down()  #up ile yaptığımız cizmen işlemini geri getir yani yazma işlemi başlar
turtle.bgcolor("gold")  #turtle arka yani panelin arka rengi ayarlar
kalem.color("red","red") #kalem nesnesinin iç ve dış rengini ilk renk iç ikinci olan dış rengi ayarlar
kalem.pensize(12) #pensize ise kalemin yani fontunu ayarlar yani kalın veya ince yazmaya yarar

kalem.left(150)  #sola kaç derece ile doneceğini ayaralar 
kalem.begin_fill()  #bize yapılan seklin içini doldurmaya yarar
for x in range(7):
    kalem.forward(37)  # kalp şeklinin  sol üst kısmının yapım sağlar 
    kalem.right(2)

for x in range(20):
    
    kalem.forward(25) # kalp şeklini sol alt kısmı
    kalem.right(10)

kalem.left(120) 

for x in range(19):
    
    kalem.forward(23) # kalp şeklini sağ üst kısmı
    kalem.right(10)

for x in range(6):
    kalem.forward(49) # kalp şeklini sağ alt kısmı
    kalem.right(2)

kalem.end_fill() #boyama işleminin bitmesini sağlar

turtle.done()# panelin açık kalmasını sağlar 
