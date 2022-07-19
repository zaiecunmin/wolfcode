import pygame
import sys
def user(how):
    d={'wolf':['class game'],'https://blog.csdn.net/jasper_ding/article/details/101608901':['class MyControl','class Button']}
    if how == 'r':
        return d
    elif how == 'p':
        print(str(d))
class game:
    def init(self,width,height,name='WolfCode'):
        pygame.init()
        pygame.mixer.init()
        color = (255, 255, 255)
        pygame.display.set_caption(name)
        size = (width, height)  # 尺寸
        screen = pygame.display.set_mode(size)
        #screen.fill([255, 255, 255])
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("arial", 16)
        font_height = font.get_linesize()
        rdict = {'screen':screen,'size':size,'font_height':font_height,'clock':clock,'font':font,'color':color}
        return rdict
    def easy(self,clock):
        while (True):
            clock.tick(60)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
            pygame.display.update()  # 显示
        pygame.quit()
        return 0
    def things(self):
        return pygame.event.get()
    def exitth(self,event):
        if (event.type == pygame.QUIT):
            sys.exit()
        return 0
    def go_things(self):
        pygame.display.flip()
    def set_picture(self,path):
        return pygame.image.load(path)
    def picture(self,picture,screen,x,y):
        screen.blit(picture,(x,y))
        pygame.display.update()
        return 0
    def icon_picture(self):
        pygame.display.set_icon()
    def keydown(self):
        return pygame.KEYDOWN
    def keydown(self,event):
        return event.key
    def button(self,screen,color,xy,wh,long):
        pygame.draw.rect(screen, color, xy+wh, long)
    def music(self,things,data):
        if things == 'play':
            pygame.mixer.music.play()#  开始播放音乐流
        elif things == 'load':
            pygame.mixer.music.load(data)#  载入一个音乐文件用于播放
            pygame.mixer.music.set_volume(0.2)
        elif things == 'stop':
            pygame.mixer.music.stop()#  结束音乐播放
        elif things == 'pause':
            pygame.mixer.music.pause()# 暂停音乐播放
        elif things == 'fadeout':
            pygame.mixer.music.fadeout(data)# 淡出的效果结束音乐播放
        elif things == 'volume':
            pygame.mixer.music.set_volume(data)# 设置音量
        elif things == 'get_volume':
            return pygame.mixer.music.get_volume()# 设置音量
        elif things == 'queue':
            pygame.mixer.music.queue(data)#  将一个音乐文件放入队列中，并排在当前播放的音乐之后


class MyControl(object):
    def __init__(self, rect, img_file, img_cx, text, font_info):
        self.status = 0
        self.rect = rect
        self.img_cx = img_cx
        self.text = text
        self.font_info = font_info

        # 设定底图，每一种 status 一张。
        if img_file is None:
            self.__img = None
            self.img_width = 0
        else:
            self.__img = pygame.image.load(img_file)
            self.__image = []

            img_rect = self.__img.get_rect()
            width = int(img_rect.width / img_cx)

            x = 0
            for i in range(self.img_cx):
                self.__image.append(self.__img.subsurface((x, 0), (width, img_rect.height)))
                x += width

            self.img_width = width

        # 设定 Lable 对象
        if text == "":
            self.label = None
        else:
            self.label = Label(rect.left, rect.top, text, font_info)

    def render(self, surface):
        if self.status >= 0:
            if self.__img is not None:
                if self.status < self.img_cx:
                    surface.blit(self.__image[self.status], (self.rect.left, self.rect.top))

            if self.label is not None:
                self.label.render(surface)

    def is_over(self, point):
        if self.status <= 0:
            bflag = False  # disabled
        else:
            bflag = self.rect.collidepoint(point)

        return bflag

    def check_click(self, event):
        if event.type == MOUSEBUTTONDOWN:
            return self.is_over(event.pos)

    def hide(self):
        self.status = -1

    def disabled(self):
        self.status = 0

    def enabled(self):
        self.status = 1
class Button(MyControl):
    def __init__(self, btn_name, event_id, rect, img_file, img_cx, text="", font_info=None):
        MyControl.__init__(self, rect, img_file, img_cx, text, font_info)

        self.event_id = event_id
        self.name = btn_name

        # 调整文字的位置为居中
        if self.label is not None:
            x = rect.left + int(rect.width / 2)
            y = rect.top + int(rect.height / 2)
            self.label.set_pos(x, y, 1, 1)

        self.status = 1

    def set_text(self, text):
        self.label.set_text(text)

    def update(self, event):
        if self.check_click(event):
            data = {"from_ui": self.name, "status":self.status}
            ev = pygame.event.Event(self.event_id, data)
            pygame.event.post(ev)
if __name__ == '__main__':
    first = game()
    d = first.init(320,420,name='main')
    while True:
        for event in first.things():
            first.exitth(event)
        first.go_things()
