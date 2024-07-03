
import turtle
import time
import random #gera numeros aleatórios
import winsound # tocar sons 

delay = 0.1 # tempo de espera entre cada movimento da cobra

score=0 #pontuação atual do jogador 
high_score=0  #maior pontuação registrada

#configurações de tela
wn=turtle.Screen()
wn.title("trabalho final-jogo de cobra")
wn.bgcolor("#D1A9A9")
wn.setup(width=600, height=600)
wn.tracer(0) #Controla a atualização da tela (0 para desativar animação automática)

#a cabeça de cobra
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop" #Define a direção inicial como parada

#comida de cobra
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[] #armazenar os segmentos do corpo da cobra

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#funções de movimento de cobra
def go_up():
    if head.direction != "down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"

def move(): #move a cabeça de cobra na direção 
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
        
#controles de teclado
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#função de som
def play_sound(sound_file, time=0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)
play_sound("The-Pink-Panther-Theme-Music-موسيقى-النمر-الوردي.wav")

while True:
    wn.update() #atualização da tela

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290: #se a cabeça da cobra toca as boras da janela
        time.sleep(1) #o jogo pausa por 1 segundo
        head.goto(0,0) #reposicionar no centro da tela
        head.direction="stop" # não se mover antes de começar jogar

        for segment in segments:
            segment.goto(1000,1000) 

        segments.clear() #remover os segmentos da cobra

        score=0 #pontuação atual é redefinida para 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) #A pontuação exibida na tela é atualizada para refletir a pontuação atual e a maior pontuação registrada.


    if head.distance(food)<20: #determinar se a cobra "comeu" a comida.
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.goto(x,y) 
        #A comida é movida para uma nova posição aleatória na tela

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("brown")
        new_segment.penup()
        segments.append(new_segment)
        #adicionar um novo segmento ao corpo da cobra
        delay -= 0.001

        score+=10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))
        #Atualização da Pontuação na Tela
    
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))


    time.sleep(delay)

wn.mainloop()
