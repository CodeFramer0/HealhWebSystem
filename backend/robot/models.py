from django.db import models
from django.utils import timezone


class TelegramUser(models.Model):
    group_choices = (
        ('player', 'Игрок'),
        ('admin', 'admin')
    )

    language_choices = (
        ('ru', 'Русский'),
        ('en', 'English')
    )

    name = models.CharField(verbose_name='Имя',max_length=30,default='Jone')
    spent_balance = models.IntegerField(verbose_name='Потрачено токенов',default=0)
    nick_name = models.CharField(verbose_name='Ник',max_length=32,default='Jone')
    balance = models.IntegerField(verbose_name='Баланс',default=5000)
    date_join = models.DateTimeField(verbose_name='Дата создания')
    chat_id = models.CharField(max_length=100,verbose_name='User/Chat ID')
    language = models.CharField(choices = language_choices, verbose_name = 'Язык', max_length = 10, default=language_choices[0][0])
    group = models.CharField(choices=group_choices, verbose_name='Группа', default=group_choices[0][0], max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f"{self.nick_name} - {self.name} - {self.chat_id}"


class GameStatistic(models.Model):
    game_choices = (
        ('dice', 'Кубики'),
        ('one_by_ten', 'Один из Десяти'),
        ('roulette', 'Мини Рулетка'),
        ('war', 'Война'),
        ('crash', 'CRASH'),
        ('dice_amount', 'Dice'),
        ('sapper', 'Сапёр'),
        ('tic_tac_toe','Крестики нолики'),
        ('slots','Слоты'),
        ('slots_1','Слоты Фрукты'),
        ('slots_2','Слоты Элементы'),
        ('slots_3','Слоты Океан'),
        ('slots_4','Слоты Счастливые Фрукты')

    )


    date = models.DateField(auto_now_add=True, verbose_name='Дата игры')
    time = models.TimeField(auto_now_add=True, verbose_name='Время игры')
    player = models.ForeignKey(TelegramUser, verbose_name='Игрок', on_delete=models.CASCADE)
    game_name = models.CharField(choices=game_choices, verbose_name='Игра', max_length=50)
    bet = models.IntegerField(verbose_name='Ставка')
    win = models.IntegerField(verbose_name='Выйгрыш')

    class Meta:
        verbose_name = 'Статистика по игре'
        verbose_name_plural = 'Статистика по играм'

    def __str__(self) -> str:
        return f"Пользователь: {self.player.balance}  Игра: {self.game_name}"
    
    
class Referals(models.Model):
    owner = models.ForeignKey(TelegramUser, verbose_name='Владелец ссылки', related_name='owner', on_delete=models.CASCADE)
    referal = models.ForeignKey(TelegramUser, verbose_name='Реферал', related_name='referal', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Реферал'
        verbose_name_plural = 'Рефералы'


class Language(models.Model):


    func = models.TextField(verbose_name='Название функции')
    ru = models.TextField(verbose_name='Русский текст')
    en = models.TextField(verbose_name='Английский текст')


    class Meta:
        verbose_name = 'Текст функции'
        verbose_name_plural = 'Текст функций'

    def __str__(self) -> str:
        return f"{self.func}"
    
    
    
    
    
class Product(models.Model):
    title = models.CharField(verbose_name = 'Название', max_length=50)
    dimes = models.IntegerField(verbose_name = 'Даймы')
    ru_price = models.FloatField(verbose_name='Цена в Рублях', default=0)
    usd_price = models.FloatField(verbose_name='Цена в Долларах', default=0)
    is_active = models.BooleanField(verbose_name = 'Вкл/Выкл', default = True)
    
    
    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'
    
    def __str__(self) -> str:
        return f"{self.title}-{self.ru_price}-{self.usd_price}"
    
    
    
    
    
    
    
    
    
class Order(models.Model):
    status_choices = (
        ('created', 'Создан'),
        ('in_process', 'В процессе'),
        ('success', 'Оплачен'),
        ('expired', 'Срок оплаты истек'),
        ('hold','Оплачено, средства заморожены'),
        ('enrolled','Баланс зачислен пользователю'),
        ('enrollment_error','Ошибка зачисления'),
        ('canceled', 'Отменен')
    )
    date = models.DateField(auto_now_add=True, verbose_name='Дата игры')
    time = models.TimeField(auto_now_add=True, verbose_name='Время игры')
    buyer = models.ForeignKey(TelegramUser, verbose_name='Покупатель', null=True, on_delete=models.DO_NOTHING)
    amount = models.FloatField(verbose_name='Сумма')
    currency = models.CharField(max_length = 30, verbose_name = 'Валюта')
    desc = models.TextField(verbose_name = 'Описание')
    lang = models.CharField(verbose_name = 'Язык', max_length=10)
    status = models.CharField(choices=status_choices, verbose_name='Статус', max_length=50)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.SET_NULL, null=True, related_name='products')
    test = models.BooleanField(verbose_name = 'Тестовый платеж', default = False)
    test_success = models.BooleanField(verbose_name = 'Результат тестового платежа', default = False)
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    
    def __str__(self) -> str:
        return f"{self.id}-{self.buyer}-{self.status}"
    



