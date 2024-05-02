from django.contrib import admin

from .models import TelegramUser, GameStatistic, Language, Order, Product, Referals



@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['nick_name','name', 'group', 'balance','spent_balance', 'id','chat_id','date_join', 'language']
    readonly_fields = ('nick_name','name','id','chat_id','date_join','spent_balance', 'language')

@admin.register(GameStatistic)
class GameStatisticAdmin(admin.ModelAdmin):
    list_display = ['date','time','player','game_name', 'bet','win']
    readonly_fields = ('date','time','player','game_name', 'bet','win')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['func', 'ru', 'en']
    search_fields = ['func']
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'id', 'buyer', 'status', 'product']
    search_fields = ['id', 'buyer__nick_name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dimes', 'ru_price', 'usd_price']
    
    
    
    
@admin.register(Referals)
class ReferalsAdmin(admin.ModelAdmin):
    list_display = ['owner', 'referal']
