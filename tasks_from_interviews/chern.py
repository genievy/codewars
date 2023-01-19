

class Ball:
    def __init__(self, a="regular"):
        self.ball_type = a


ball1 = Ball()
ball2 = Ball("super")

print(ball2.ball_type)
print(ball1.ball_type)