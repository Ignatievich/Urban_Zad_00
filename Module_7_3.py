""" Module_7_2_0
Домашнее задание по теме "Оператор "with".
==========================================
Цель: применить на практике оператор with,
вспомнить написание кода в парадигме ООП.
------------------------------------------
ЗАДАЧА "Найдёт везде":
"""
class WordsFinder :
    file_names = []
    def __init__( self, *file_names ) :
        self.file_names = file_names

    def get_all_words( self ) :
        allSlovar = {}
        for nameFile in self.file_names :
            with open( nameFile, 'r', encoding='utf-8') as file:
                filStroka = file.read()  # Считываем содержимое текстового файла
                filStroka = filStroka.lower()   # "Чистим" строки из файлов
                filStroka = filStroka.replace('!', ' ' )
                filStroka = filStroka.replace('?', ' ' )
                filStroka = filStroka.replace(',', ' ' )
                filStroka = filStroka.replace('.', ' ' )
                filStroka = filStroka.replace(':', ' ' )
                filStroka = filStroka.replace(';', ' ' )
                filStroka = filStroka.replace('=', ' ' )
                filStroka = filStroka.replace('-', ' ' )
                filStroka = filStroka.replace('\n', ' ' )
                filStroka = filStroka.replace('  ', ' ' )
                filStroka = filStroka.rstrip()  # Очищаем строку от конечного пробела
                filSpisok = filStroka.split( ' ' )  # Расщепляем строку по словам
            allSlovar[nameFile] = filSpisok  # Запихиваем список в словарь!
        return allSlovar

    # word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.
    def find( self, word ) :
        allSlovar = self.get_all_words()
        fndSlovo  = {}
        for filItem in allSlovar :
            filZnch = allSlovar.get(filItem)
            word = word.lower()
            for i, s in enumerate( filZnch ) :
                if word == s :
                    fndSlovo[filItem] = i+1
                    break
        result = fndSlovo
        return result

    # word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла.
    def count( self, word ) :
        allSlovar = self.get_all_words()
        fndSlovo = {}
        for filItem in allSlovar:
            filZnch = allSlovar.get(filItem)
            word = word.lower()
            n = 0
            for i, s in enumerate(filZnch):
                if word == s:
                    n += 1
                    fndSlovo[filItem] = n
        result = fndSlovo
        return result

#=== Пример выполнения программы: =============================
finder1 = WordsFinder('test_file.txt')
print( finder1.get_all_words() )  # Все слова
print(finder1.find('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего
print()
finder2 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')    ##
print( finder2.get_all_words() )  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
#==============================================================
