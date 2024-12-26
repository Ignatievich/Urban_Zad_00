"""
Дополнительное практическое задание по модулю: "Классы и объекты."
==================================================================
Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.
--------------------------------------------------------------------------------------
ЗАДАНИЕ "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться
    дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.).
    Конечно же для старта написания интернет ресурса требуются хотя бы базовые
    знания программирования.
Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов,
    которые будут выполнять похожий функционал на сайте.
Всего будет 3 класса: UrTube, Video, User.
---------------------------------------------------------------------------------------
Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет
    содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

"""
from time import sleep

class User :
    def __init__( self, *args ) : pass

class Video :
    def __init__( self, title, duration, **kwargs) :
        self.title    = title       # Заголовок видео
        self.duration = duration    # Продолжительность (секунды)
        self.time_now = 0           # Секунда остановки (изначально 0)
        self.adult_mode = kwargs.get( 'adult_mode' )  # Ограничение по возрасту,
        if self.adult_mode == None :
            self.adult_mode = False  # Ограничение по возрасту по умолчанию

class UrTube :
    def __init__( self ) :
        self.users  = []        # Список объектов класса User
        self.videos = []        # Список объектов класса Video
        self.vidYes = []        # Список найденных объектов Video
        self.current_user  = None   # Текущий пользователь (Указатель на объект User)
        self.current_video = None   # Текущее видео (Указатель на объект Video)

    # Метод добавляет пользователя в список, если пользователя не существует.
    # Если пользователь существует, выводит "Пользователь {nickname} уже существует".
    # После регистрации вход выполняется автоматически.
    def register(self, nickname, password, age):
        user  = ( nickname , hash( password ), age )    # Создаю кортеж с данными пользователя
        n = None
        for i, usr in enumerate( self.users ) :
            if user[0] == self.users[i][0] :
                n = i
        if n == None :
            self.users.append( user )  # Регистрируем нового пользователя!
            self.current_user = user  # После регистрации, вход выполняется автоматически
        else :
            print( f'Пользователь {user[0]} уже существует ' )
            self.log_in( nickname, password )
    def log_in( self, nickname, password ) :
        usr = ( nickname , hash( password ) )   # Создаю кортеж с данными пользователя без возраста!
        if ( self.current_user != None )  :  # Если текущий пользователь есть
            current_usr = self.current_user[:-1]
            if usr == current_usr: # Проверяем является ли пользователь уже текущим?
                print( f'Пользователь {usr[0]} уже в системе!' )
                return
        else : # Если пользователь не является текущим!
            for i, us_r in enumerate( self.users ) :
                if usr[0] == us_r[0] :      # Если пользователь зарегистрирован
                    if usr[1] == us_r[1] :  # Проверка правильности пароля
                        self.current_user = self.users[i]   # Меняем текущего пользователя
                        print( f'Здравствуйте {usr[0]}! Вы вошли в систему!' )
                    else :
                        print( f'Пользователь {usr[0]}! Вы ввели неверный пароль!'  )

    # Метод для сброса текущего пользователя на None.
    def log_out( self ) :
        self.current_user = None

    # Метод который принимает неограниченное количество объектов класса Video
    # и все добавляет в videos, если видео с таким же названием не существует.
    # В противном случае ничего не происходит.
    def add( self, *args ) :
        self.videos += list( args )

    # Метод принимает поисковое слово и возвращает список названий всех видео,
    # содержащих поисковое слово. Учесть, что слово 'UrbaN' присутствует
    # в строке 'Urban the best' (не учитывать регистр).
    def get_videos( self, search ) :
        vidTit = []                     # Список названий найденный видео!
        srch = search.strip()   # Убираем пробелы вначале и в конце названия искомого слова
        self.search = srch.lower()      # Переводим искомое слово в нижний регистр
        for i, vid in enumerate( self.videos ) :
            t = vid.title.strip()
            tit = t.lower()
            if self.search in tit :
                vidTit.append( vid.title )
        return vidTit

    # Метод, который принимает название фильма, если не находит точного
    # совпадения (вплоть до пробела), то ничего не воспроизводится,
    # если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    # После текущее время просмотра данного видео сбрасывается.
    def watch_video( self, title ) :
        View = False
        if self.current_user == None :
            print( 'Войдите в аккаунт, чтобы смотреть видео' )
        else :
            if self.search_video( title ) : # Если видео с title нашлось!
                if self.current_video.adult_mode == True :
                    if  self.current_user[2] >= 18 :     # Если пользователь старше 18-ти лет
                        View = True
                    else :
                        print( f'Пользователь {self.current_user[0]}, вам нет 18 лет, пожалуйста покиньте страницу!' )
                else :
                    View = True
                if View :
                    for sec in range( 0, self.current_video.duration ) :
                        print( ' ', sec , end='' )
                        sleep( 1 )
                    print( ' Конец видео' )
            else :
                print( 'Видео с таким названием не нашлось!' )

    # Метод для определения наличия видео с заданным названием в списке видео
    # Возвращает True если видео в списке найдено и устанавливает найденное видео в текущее!
    def search_video( self, title ) :
        t = title.strip()   # Убираем случайные пробелы в начале и в конце названия
        self.title = t.lower()   # Переводим название в нижний регистр
        flgYes = False     ##
        for vid in self.videos :  # Перебираем все видео в списке
            v = vid.title.strip()       # Убираем пробелы вначале и в конце
            v = v.lower()               # Переводим название в ниж. регистр
            if self.title == v :
                self.current_video = vid        #
            if v == self.title  :
                flgYes = True
        return flgYes

#=====================================================================================
#== Код для проверки: ================================================================
ur = UrTube()       # Создаём объект Ur
v1 = Video('Лучший язык программирования 2024 года', 20) # Заменить на 200 !!!
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True) #

#== Добавление видео
ur.add(v1, v2)

#== Проверка поиска
print( ur.get_videos('лучший') )
print( ur.get_videos('ПРОГ') )

#== Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

#== Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
print(ur.current_user[0])

#== Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

