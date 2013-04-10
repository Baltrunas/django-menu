# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from menu.models import Item

class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Item, ItemTranslationOptions)