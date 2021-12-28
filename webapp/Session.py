def Session():
    """A class to describe a shooting session

    Attributes:
        id - (int) Session ID
        id_user - (int) Related user ID
        percentage_target - (float) Percentage to achive
        shots - [float] Shots points 
        duration - (int) Sesion lenght in seconds
    """

    def __init__(self, id, id_user, percentage_target, shots, score, duration):
        self.id = id
        self.id_user = id_user
        self.percentage_target = percentage_target
        self.shots = shots
        self.score = score
        self.duration = duration