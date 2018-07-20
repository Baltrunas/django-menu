from modeltranslation.translator import translator, TranslationOptions

from .models import Group, Item


class GroupTranslationOptions(TranslationOptions):
	fields = ['name']

translator.register(Group, GroupTranslationOptions)


class ItemTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(Item, ItemTranslationOptions)
