import pygame
import sys

SCREEN_WIDTH=840
SCREEN_HEIGHT=480

WHITE=(255,255,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
BLACK=(0,0,0)

pos_x=420
pos_y=240

p1_x=100
p1_y=240
p2_x=740
p2_y=240

def selectGame():
    global screen,clock,select,info
    screen.blit(select,(0,0))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        key_event=pygame.key.get_pressed()
        if key_event[pygame.K_SPACE]:
            readyGame()
        if key_event[pygame.K_c]:
            infoGame()
        pygame.display.update()

def infoGame():
    global screen,info
    screen.blit(info,(0,0))
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        key_event=pygame.key.get_pressed()
        if key_event[pygame.K_ESCAPE]:
            selectGame()
        pygame.display.update()    

vel1=7 #1P Velocity
vel2=7 #2P Velocity


def readyGame():
    global screen,ball,p1,p2
    myfont2 = pygame.font.SysFont('Arial', 120)
    screen.fill(GREEN)
    pygame.draw.rect(screen,WHITE,[(SCREEN_WIDTH/2)-1,0,2,480],0)
    pygame.draw.arc(screen,WHITE,[320,140,200,200],0,360,2)
    pygame.draw.rect(screen,WHITE,[0,140,100,200],2)
    pygame.draw.rect(screen,WHITE,[740,140,100,200],2)
    screen.blit(ball,(380,200))
    screen.blit(p1,(75,210))
    screen.blit(p2,(715,210))
    textsurface2 = myfont2.render("READY 3", True, (255, 0, 0))
    screen.blit(textsurface2,(215,160))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill(GREEN)
    pygame.draw.rect(screen,WHITE,[(SCREEN_WIDTH/2)-1,0,2,480],0)
    pygame.draw.arc(screen,WHITE,[320,140,200,200],0,360,2)
    pygame.draw.rect(screen,WHITE,[0,140,100,200],2)
    pygame.draw.rect(screen,WHITE,[740,140,100,200],2)
    screen.blit(ball,(380,200))
    screen.blit(p1,(75,210))
    screen.blit(p2,(715,210))
    textsurface2 = myfont2.render("READY 2", True, (255, 0, 0))
    screen.blit(textsurface2,(215,160))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill(GREEN)
    pygame.draw.rect(screen,WHITE,[(SCREEN_WIDTH/2)-1,0,2,480],0)
    pygame.draw.arc(screen,WHITE,[320,140,200,200],0,360,2)
    pygame.draw.rect(screen,WHITE,[0,140,100,200],2)
    pygame.draw.rect(screen,WHITE,[740,140,100,200],2)
    screen.blit(ball,(380,200))
    screen.blit(p1,(75,210))
    screen.blit(p2,(715,210))
    textsurface2 = myfont2.render("READY 1", True, (255, 0, 0))
    screen.blit(textsurface2,(215,160))
    pygame.display.update()
    pygame.time.wait(1000)
    runGame()





def runGame():
    global screen,p1,p2,p12,p22,ball,clock,p1_x,p1_y,p2_x,p2_y,pos_x,pos_y,goal1,goal2,win,lose
    myfont = pygame.font.SysFont('Arial', 80)
    myfont2 = pygame.font.SysFont('Arial', 120)
    pMode1=0
    pMode2=0
    score1=0
    score2=0
    vel_x=0
    vel_y=0
    acc_x=0
    acc_y=0
    vec=5
    judgeRage=55
    boost1=True
    boost2=True
    

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            
            if event .type == pygame.KEYDOWN:  
                if event.key==pygame.K_z:
                    boost1=False
            if event .type == pygame.KEYUP:  
                if event.key==pygame.K_z:
                    boost1=True
            
            if event .type == pygame.KEYDOWN:  
                if event.key==pygame.K_SLASH:
                    boost2=False
            if event .type == pygame.KEYUP:  
                if event.key==pygame.K_SLASH:
                    boost2=True

        key_event=pygame.key.get_pressed()
        if key_event[pygame.K_d] and p1_x>=25:
            p1_x-=vel1
            pMode1+=1
            if (p1_y>p2_y-60 and p1_y<p2_y+60) and (p1_x<=p2_x+50 and p1_x>p2_x+25):
                p1_x+=vel1
        if key_event[pygame.K_g] and p1_x<=815:
            p1_x+=vel1
            pMode1+=1
            if (p1_y>p2_y-60 and p1_y<p2_y+60) and (p1_x>=p2_x-50 and p1_x<p2_x-25):
                p1_x-=vel1
        if key_event[pygame.K_r] and p1_y>=30:
            p1_y-=vel1
            pMode1+=1
            if (p1_x>p2_x-50 and p1_x<p2_x+50) and (p1_y<=p2_y+60 and p1_y>p2_y+30):
                p1_y+=vel1
        if key_event[pygame.K_f] and p1_y<=450:
            p1_y+=vel1
            pMode1+=1
            if (p1_x>p2_x-50 and p1_x<p2_x+50) and (p1_y>=p2_y-60 and p1_y<p2_y-30):
                p1_y-=vel1



        if (p1_y>=pos_y and p1_y<pos_y+(judgeRage+5)) and (p1_x<=pos_x+judgeRage and p1_x>pos_x) and boost1==False:
            vel_x=-4
            vel_y=-2
            acc_x=-8
            acc_y=-(8-2)
            pMode1+=1
            p1_x+=vec*2
            p1_y+=(vec/2)*2
        if (p1_y>pos_y-(judgeRage+5) and p1_y<pos_y) and (p1_x<=pos_x+judgeRage and p1_x>pos_x) and boost1==False:
            vel_x=-4
            vel_y=2
            acc_x=-8
            acc_y=(8-2)
            p1_x+=vec*2
            p1_y-=(vec/2)*2            
        if (p1_y>=pos_y and p1_y<pos_y+(judgeRage+5)) and (p1_x>=pos_x-judgeRage and p1_x<pos_x) and boost1==False:
            vel_x=4
            vel_y=-2
            acc_x=8
            acc_y=-(8-2)
            p1_x-=vec*2
            p1_y+=(vec/2)*2            
        if (p1_y>pos_y-(judgeRage+5) and p1_y<pos_y) and (p1_x>=pos_x-judgeRage and p1_x<pos_x) and boost1==False:
            vel_x=4
            vel_y=2
            acc_x=8
            acc_y=(8-2)
            p1_x-=vec*2
            p1_y-=(vec/2)*2

        if (p1_x>pos_x-judgeRage and p1_x<pos_x) and (p1_y<=pos_y+(judgeRage+5) and p1_y>pos_y) and boost1==False:
            vel_x=2
            vel_y=-4
            acc_x=(8-2)
            acc_y=-8
            p1_x-=(vec/2)*2
            p1_y+=vec
        if (p1_x>=pos_x and p1_x<pos_x+judgeRage) and (p1_y<=pos_y+(judgeRage+5) and p1_y>pos_y) and boost1==False:
            vel_x=-2
            vel_y=-4
            acc_x=-(8-2)
            acc_y=-8
            p1_x+=(vec/2)*2
            p1_y+=vec            
        if (p1_x>pos_x-judgeRage and p1_x<=pos_x) and (p1_y>=pos_y-(judgeRage+5) and p1_y<pos_y) and boost1==False:
            vel_x=2
            vel_y=4
            acc_x=(8-2)
            acc_y=8
            p1_x-=(vec/2)*2
            p1_y-=vec
        if (p1_x>=pos_x and p1_x<pos_x+judgeRage) and (p1_y>=pos_y-(judgeRage+5) and p1_y<pos_y) and boost1==False:
            vel_x=-2
            vel_y=4
            acc_x=-(8-2)
            acc_y=8
            p1_x+=(vec/2)*2
            p1_y-=vec            


        if (p2_y>=pos_y and p2_y<pos_y+judgeRage) and (p2_x<=pos_x+judgeRage and p2_x>pos_x) and boost2==False:
            vel_x=-4
            vel_y=-2
            acc_x=-8
            acc_y=-(8-2)
            p2_x+=vec*2
            p2_y+=(vec/2)*2
        if (p2_y>pos_y-judgeRage and p2_y<=pos_y) and (p2_x<=pos_x+judgeRage and p2_x>pos_x) and boost2==False:
            vel_x=-4
            vel_y=2
            acc_x=-8
            acc_y=(8-2)
            p2_x+=vec*2
            p2_y-=(vec/2)*2
        if (p2_y>=pos_y and p2_y<pos_y+judgeRage) and (p2_x>=pos_x-judgeRage and p2_x<pos_x) and boost2==False:
            vel_x=4
            vel_y=-2
            acc_x=8
            acc_y=-(8-2)
            p2_x-=vec*2
            p2_y+=(vec/2)*2
        if (p2_y>pos_y-judgeRage and p2_y<=pos_y) and (p2_x>=pos_x-judgeRage and p2_x<pos_x) and boost2==False:
            vel_x=4
            vel_y=2
            acc_x=8
            acc_y=(8-2)
            p2_x-=vec*2
            p2_y-=(vec/2)*2

        if (p2_x>pos_x-judgeRage and p2_x<=pos_x) and (p2_y<=pos_y+judgeRage and p2_y>pos_y) and boost2==False:
            vel_x=2
            vel_y=-4
            acc_x=(8-2)
            acc_y=-8
            p2_x-=(vec/2)*2
            p2_y+=vec
        if (p2_x>=pos_x and p2_x<pos_x+judgeRage) and (p2_y<=pos_y+judgeRage and p2_y>pos_y) and boost2==False:
            vel_x=-2
            vel_y=-4
            acc_x=-(8-2)
            acc_y=-8
            p2_x+=(vec/2)*2
            p2_y+=vec
        if (p2_x>pos_x-judgeRage and p2_x<=pos_x) and (p2_y>=pos_y-judgeRage and p2_y<pos_y) and boost2==False:
            vel_x=2
            vel_y=4
            acc_x=(8-2)
            acc_y=8
            p2_x-=(vec/2)*2
            p2_y-=vec
        if (p2_x>=pos_x and p2_x<pos_x+judgeRage) and (p2_y>=pos_y-judgeRage and p2_y<pos_y) and boost2==False:
            vel_x=-2
            vel_y=4
            acc_x=-(8-2)
            acc_y=8
            p2_x+=(vec/2)*2
            p2_y-=vec


    
        if key_event[pygame.K_LEFT] and p2_x>=25:
            p2_x-=vel2
            pMode2+=1
            if (p2_y>p1_y-60 and p2_y<p1_y+60) and (p2_x<=p1_x+50 and p2_x>p1_x+25):
                p2_x+=vel2
        if key_event[pygame.K_RIGHT] and p2_x<=815:
            p2_x+=vel2
            pMode2+=1
            if (p2_y>p1_y-60 and p2_y<p1_y+60) and (p2_x>=p1_x-50 and p2_x<p1_x-25):
                p2_x-=vel2
        if key_event[pygame.K_UP] and p2_y>=30:
            p2_y-=vel2
            pMode2+=1;
            if (p2_x>p1_x-50 and p2_x<p1_x+50) and (p2_y<=p1_y+60 and p2_y>p1_y+30):
                p2_y+=vel2
        if key_event[pygame.K_DOWN] and p2_y<=450:
            p2_y+=vel2
            pMode2+=1
            if (p2_x>p1_x-50 and p2_x<p1_x+50) and (p2_y>=p1_y-60 and p2_y<p1_y-30):
                p2_y-=vel2

        if p1_x<=25:
            p1_x+=7
        if p2_x<=25:
            p2_x+=7
        if p1_y<=30:
            p1_y+=7
        if p2_y<=30:
            p2_y+=7
        if p1_y>=455:
            p1_y-=7
        if p2_y>=455:
            p2_y-=7
        if p1_x>=810:
            p1_x-=7
        if p2_x>=810:
            p2_x-=7
        
        '''
        -----------------------------
        '''
        
        acc=6
        if (p1_y>=pos_y and p1_y<pos_y+(judgeRage+5)) and (p1_x<=pos_x+judgeRage and p1_x>pos_x) and boost1:
            vel_x=0
            vel_y=0
            acc_x=-acc
            acc_y=-(acc-2)
            p1_x+=vec*2
            p1_y+=(vec/2)*2
        if (p1_y>pos_y-(judgeRage+5) and p1_y<pos_y) and (p1_x<=pos_x+judgeRage and p1_x>pos_x) and boost1:
            vel_x=0
            vel_y=0
            acc_x=-acc
            acc_y=(acc-2)
            p1_x+=vec*2
            p1_y-=(vec/2)*2
        if (p1_y>=pos_y and p1_y<pos_y+(judgeRage+5)) and (p1_x>=pos_x-judgeRage and p1_x<pos_x) and boost1:
            vel_x=0
            vel_y=0
            acc_x=acc
            acc_y=-(acc-2)
            p1_x-=vec*2
            p1_y+=(vec/2)*2
        if (p1_y>pos_y-(judgeRage+5) and p1_y<pos_y) and (p1_x>=pos_x-judgeRage and p1_x<pos_x) and boost1:
            vel_x=0
            vel_y=0
            acc_x=acc
            acc_y=(acc-2)
            p1_x-=vec*2
            p1_y-=(vec/2)*2

        if (p1_x>pos_x-judgeRage and p1_x<pos_x) and (p1_y<=pos_y+(judgeRage+5) and p1_y>pos_y) and boost1:
            vel_x=0
            vel_y=0
            acc_x=(acc-2)
            acc_y=-acc
            p1_x-=(vec/2)*2
            p1_y+=vec
        if (p1_x>=pos_x and p1_x<pos_x+judgeRage) and (p1_y<=pos_y+(judgeRage+5) and p1_y>pos_y) and boost1:
            vel_x=0
            vel_y=0
            acc_x=-(acc-2)
            acc_y=-acc
            p1_x+=(vec/2)*2
            p1_y+=vec
        if (p1_x>pos_x-judgeRage and p1_x<=pos_x) and (p1_y>=pos_y-(judgeRage+5) and p1_y<pos_y) and boost1:
            vel_x=0
            vel_y=0
            acc_x=(acc-2)
            acc_y=acc
            p1_x-=(vec/2)*2
            p1_y-=vec
        if (p1_x>=pos_x and p1_x<pos_x+judgeRage) and (p1_y>=pos_y-(judgeRage+5) and p1_y<pos_y) and boost1:
            vel_x=0
            vel_y=0
            acc_x=-(acc-2)
            acc_y=acc
            p1_x+=(vec/2)*2
            p1_y-=vec

######################이 아래로 조건문 4개 : 대각선 판정 부분########################
        '''
        if (p1_y>=pos_y-(judgeRage) and p1_y<pos_y) and (p1_x<pos_x+(judgeRage*2) and p1_x>=pos_x=judgeRage):
            vel_x=0
            vel_y=0
            acc_x=-acc
            acc_y=-acc
            p1_x+=vec*2
            p1_y+=(vec)*2
        if (p1_y>=pos_y-(judgeRage*2) and p1_y<pos_y) and (p1_x<=pos_x and p1_x>pos_x-judgeRage):
            vel_x=0
            vel_y=0
            acc_x=-acc
            acc_y=-acc
            p1_x+=vec*2
            p1_y+=(vec)*2
            

'''
        if (p2_y>=pos_y and p2_y<pos_y+judgeRage) and (p2_x<=pos_x+judgeRage and p2_x>pos_x) and boost2:
            vel_x=0
            vel_y=0
            acc_x=-acc
            acc_y=-(acc-2)
            p2_x+=vec*2
            p2_y+=(vec/2)*2
        if (p2_y>pos_y-judgeRage and p2_y<=pos_y) and (p2_x<=pos_x+judgeRage and p2_x>pos_x) and boost2:
            vel_x=0
            vel_y=0
            acc_x=-acc
            acc_y=(acc-2)
            p2_x+=vec*2
            p2_y-=(vec/2)*2
        if (p2_y>=pos_y and p2_y<pos_y+judgeRage) and (p2_x>=pos_x-judgeRage and p2_x<pos_x) and boost2:
            vel_x=0
            vel_y=0
            acc_x=acc
            acc_y=-(acc-2)
            p2_x-=vec*2
            p2_y+=(vec/2)*2
        if (p2_y>pos_y-judgeRage and p2_y<=pos_y) and (p2_x>=pos_x-judgeRage and p2_x<pos_x) and boost2:
            vel_x=0
            vel_y=0
            acc_x=acc
            acc_y=(acc-2)
            p2_x-=vec*2
            p2_y-=(vec/2)*2

        if (p2_x>pos_x-judgeRage and p2_x<=pos_x) and (p2_y<=pos_y+judgeRage and p2_y>pos_y) and boost2:
            vel_x=0
            vel_y=0
            acc_x=(acc-2)
            acc_y=-acc
            p2_x-=(vec/2)*2
            p2_y+=vec
        if (p2_x>=pos_x and p2_x<pos_x+judgeRage) and (p2_y<=pos_y+judgeRage and p2_y>pos_y) and boost2:
            vel_x=0
            vel_y=0
            acc_x=-(acc-2)
            acc_y=-acc
            p2_x+=(vec/2)*2
            p2_y+=vec
        if (p2_x>pos_x-judgeRage and p2_x<=pos_x) and (p2_y>=pos_y-judgeRage and p2_y<pos_y) and boost2:
            vel_x=0
            vel_y=0
            acc_x=(acc-2)
            acc_y=acc
            p2_x-=(vec/2)*2
            p2_y-=vec
        if (p2_x>=pos_x and p2_x<pos_x+judgeRage) and (p2_y>=pos_y-judgeRage and p2_y<pos_y) and boost2:
            vel_x=0
            vel_y=0
            acc_x=-(acc-2)
            acc_y=acc
            p2_x+=(vec/2)*2
            p2_y-=vec

        
        if pos_x<=0:
            vel_x=0
            acc_x=4
        if pos_x>840:
            vel_x=0
            acc_x=-4
        if pos_y<=40:
            vel_y=0
            acc_y=4
        if pos_y>=460:
            vel_y=0
            acc_y=-4

        if acc_x>0:
            acc_x-=2
        if acc_y>0:
            acc_y-=2
        if acc_x<0:
            acc_x+=2
        if acc_y<0:
            acc_y+=2

        vel_x+=acc_x
        vel_y+=acc_y
        pos_x+=vel_x
        pos_y+=vel_y
        
        '''
        acc=6
        if (p1_y>pos_y-40 and p1_y<pos_y+40) and (p1_x<=pos_x+40 and p1_x>pos_x):
            vel_x=0
            acc_x=-acc
            p1_x+=vec
        if (p1_y>pos_y-40 and p1_y<pos_y+40) and (p1_x>=pos_x-40 and p1_x<pos_x):
            vel_x=0
            acc_x=acc
            p1_x-=vec
        if (p1_x>pos_x-40 and p1_x<pos_x+40) and (p1_y<=pos_y+40 and p1_y>pos_y):
            vel_y=0
            acc_y=-acc
            p1_y+=vec
        if (p1_x>pos_x-40 and p1_x<pos_x+40) and (p1_y>=pos_y-40 and p1_y<pos_y):
            vel_y=0
            acc_y=acc
            p1_y-=vec
        if (p2_y>pos_y-40 and p2_y<pos_y+40) and (p2_x<=pos_x+40 and p2_x>pos_x):
            vel_x=0
            acc_x=-acc
            p2_x+=vec
        if (p2_y>pos_y-40 and p2_y<pos_y+40) and (p2_x>=pos_x-40 and p2_x<pos_x):
            vel_x=0
            acc_x=acc
            p2_x-=vec
        if (p2_x>pos_x-40 and p2_x<pos_x+40) and (p2_y<=pos_y+40 and p2_y>pos_y):
            vel_y=0
            acc_y=-acc
            p2_y+=vec
        if (p2_x>pos_x-40 and p2_x<pos_x+40) and (p2_y>=pos_y-40 and p2_y<pos_y):
            vel_y=0
            acc_y=acc
            p2_y-=vec

        if pos_x<=0:
            vel_x=0
            acc_x=6
        if pos_x>840:
            vel_x=0
            acc_x=-6
        if pos_y<=40:
            vel_y=0
            acc_y=6
        if pos_y>=460:
            vel_y=0
            acc_y=-6

        if acc_x>0:
            acc_x-=2
        if acc_y>0:
            acc_y-=2
        if acc_x<0:
            acc_x+=2
        if acc_y<0:
            acc_y+=2

        vel_x+=acc_x
        vel_y+=acc_y
        pos_x+=vel_x
        pos_y+=vel_y
        '''
        #print(str(vel_x)+"/"+str(vel_y)+"/"+str(acc_x)+"/"+str(acc_y))


        '''
        if key_event[pygame.K_z]:
            vel1=7
        if key_event[pygame.K_RETURN]: 
            vel2=7
        '''


        if pos_x<=0 and (pos_y<=320 and pos_y>=160) and score2<7:
            score2+=1
            textsurface = myfont.render(str(score1)+' - '+str(score2), True, (255, 255, 255))
            screen.blit(textsurface,(355,0))
            screen.blit(goal1,(0,190))
            pygame.display.update()
            pygame.time.wait(700)
            acc_x=0
            acc_y=0
            vel_x=0
            vel_y=0
            pos_x=420
            pos_y=240
            p1_x=300#aa
            p1_y=240
            p2_x=740#aa
            p2_y=240
            
        if pos_x>=840 and (pos_y<=320 and pos_y>=160) and score1<7:
            score1+=1
            textsurface = myfont.render(str(score1)+' - '+str(score2), True, (255, 255, 255))
            screen.blit(textsurface,(355,0))
            screen.blit(goal2,(740,190))
            pygame.display.update()
            pygame.time.wait(700)
            acc_x=0
            acc_y=0
            vel_x=0
            vel_y=0
            pos_x=420
            pos_y=240
            p1_x=100#aa
            p1_y=240
            p2_x=540#aa
            p2_y=240

        if score1>=7:
            textsurface2 = myfont2.render("1P WIN !", True, (255, 0, 0))
            screen.blit(goal2,(740,190))
            #screen.blit(win,(p1_x-25,p1_y-30))
            #screen.blit(lose,(p2_x-25,p2_y-30))
            screen.blit(textsurface2,(215,160))
            pygame.display.update()
            pygame.time.wait(2000)
            score1=0
            score2=0
            selectGame()

        if score2>=7:
            textsurface2 = myfont2.render("2P WIN !", True, (255, 0, 0))
            screen.blit(goal1,(0,190))
            #screen.blit(win,(p2_x-25,p2_y-30))
            #screen.blit(lose,(p1_x-25,p1_y-30))
            screen.blit(textsurface2,(215,160))
            pygame.display.update()
            pygame.time.wait(2000)
            score1=0
            score2=0
            selectGame()

                

    
        screen.fill(GREEN)
        pygame.draw.rect(screen,WHITE,[(SCREEN_WIDTH/2)-1,0,2,480],0)
        pygame.draw.arc(screen,WHITE,[320,140,200,200],0,360,2)
        pygame.draw.rect(screen,WHITE,[0,140,100,200],2)
        pygame.draw.rect(screen,WHITE,[740,140,100,200],2)
        
        #pygame.draw.circle(screen,BLACK,(pos_x,pos_y),40)
        screen.blit(ball,(pos_x-40,pos_y-40))
        #textsurface = myfont.render(str(score1)+' - '+str(score2), True, (255, 255, 255))
        #screen.blit(textsurface,(355,0))

        if pMode1%2==0:
            screen.blit(p1,(p1_x-25,p1_y-30))
        if pMode1%2==1:
            screen.blit(p12,(p1_x-25,p1_y-30))
        if pMode2%2==0:
            screen.blit(p2,(p2_x-25,p2_y-30))
        if pMode2%2==1:
            screen.blit(p22,(p2_x-25,p2_y-30))
    
        pygame.display.update()
        

def initGame():
    global background,screen, p1,p2,p12,p22,ball,clock,select,info,goal1,goal2,win,lose
    pygame.init()
    pygame.display.set_caption("Pikachu Soccer")
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    
    background=pygame.image.load('grass.png')
    p1=pygame.image.load('p1.png')
    p2=pygame.image.load('p2.png')
    p12=pygame.image.load('p12.png')
    p22=pygame.image.load('p22.png')
    ball=pygame.image.load('ball.png')
    select=pygame.image.load('select.png')
    info=pygame.image.load('info2.png')
    goal1=pygame.image.load('goal1.png')
    goal2=pygame.image.load('goal2.png')
    win=pygame.image.load('win.png')
    lose=pygame.image.load('lose.png')

    clock=pygame.time.Clock()
    selectGame()
initGame()