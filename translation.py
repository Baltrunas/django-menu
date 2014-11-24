from modeltranslation.translator import translator, TranslationOptions

from .models import Item


class ItemTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(Item, ItemTranslationOptions)
