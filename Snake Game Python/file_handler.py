class FileHandler:
    def save_high_score(self, score):
        with open("highscore.txt", "w") as file:
            file.write(str(score))

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0
