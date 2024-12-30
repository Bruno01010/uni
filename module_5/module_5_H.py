import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        self.age = age

    def __repr__(self):
        return f'<User(nickname="{self.nickname}", age={self.age})>'

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'<Video(title="{self.title}", duration={self.duration}, time_now={self.time_now}, adult_mode={self.adult_mode})>'

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users.append(new_user)
            self.log_in(nickname, password)
            print(f"Учетная запись {nickname} успешно создана.")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                continue
            self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        results = [video.title for video in self.videos if search_word in video.title.lower()]
        return results

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = next((video for video in self.videos if video.title == title), None)
        if found_video is None:
            print(f"Видео '{title}' не найдено.")
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for i in range(found_video.time_now + 1, found_video.duration + 1):
            print(i)
            time.sleep(1)
        found_video.time_now = 0
        print("Конец видео")

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


ur.add(v1, v2)


print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


ur.watch_video('Лучший язык программирования 2024 года!')