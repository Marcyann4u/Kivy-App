from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class Player(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        new_x = self.pos[0] + self.velocity_x  # Calcula a nova posição X
        # Impõe os limites da tela (largura mínima e máxima)
        new_x = max(0, new_x)  # Impõe limite mínimo
        new_x = min(Window.width - self.width, new_x)  # Impõe limite máximo
        
        # Inverte a velocidade horizontal se atingir as bordas
        if new_x == 0 or new_x == Window.width - self.width:
            self.velocity_x *= -1
        
        self.pos = (new_x, self.pos[1])  # Define a nova posição X


class FlappyGame(Widget):
    def __init__(self, **kwargs):
        super(FlappyGame, self).__init__(**kwargs)
        self.player = Player(center=(Window.width * 0.5, Window.height * 0.3))  # Posição ajustada
        self.add_widget(self.player)
        
        self.velocity_x = 0  # Velocidade de movimento horizontal inicial
        
        Clock.schedule_interval(self.update, 1 / 60.0)  # Atualiza a cada 1/60 segundos (60 FPS)

    def update(self, dt):
        self.player.velocity_x = self.velocity_x
        self.player.move()  # Chamada para a função de movimento

class FlappyApp(App):
    def build(self):
        return FlappyGame()

if __name__ == '__main__':
    FlappyApp().run()