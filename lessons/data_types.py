class Profile:
    username: str
    bio: str
    followers: int
    following: int
    private: bool

    def __init__(self):
        self.username = "usr9"
        self.bio = ""
        self.follower = 0
        self.following = 0
        self.private = False
