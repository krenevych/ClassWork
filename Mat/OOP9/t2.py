from abc import ABCMeta, abstractmethod

class FileReaderListener(metaclass=ABCMeta): # інтерфейс
    @abstractmethod
    def onReceive(self, line: str):
        # призначений для обміну повідомленнями
        # між слухачами і об'єктом за яким спостерігають
        # (який слухають)
        pass

class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.listeners = set()  # список слухачів, тобто
        # екземплярів класів, що реалізують інтерфейс FileReaderListener

    def registerListener(self, listener: FileReaderListener):
        assert isinstance(listener, FileReaderListener)
        self.listeners.add(listener)

    def notifyListeners(self, line):
        for listener in self.listeners:
            listener.onReceive(line) # відправити слухачу прочитаний рядок файлу line

    def read(self):
        with open(self.file_name) as f:
            for line in f:
                self.notifyListeners(line)

class FilePrinter(FileReaderListener):
    """ Слухач, що реалізує задачу:
    •	Виведіть усі прочитані рядки на екран
    """
    def onReceive(self, line):
        print(line[:-1])

class WordCounter(FileReaderListener):
    """ Слухач, що реалізує задачу:
    •	Підрахуйте кількість слів у текстовому файлі
    """

    def __init__(self):
        self.word_counter = 0

    def onReceive(self, line):
        words = line.split()
        self.word_counter += len(words)

    def showResult(self):
        print("кількість слів у прочитаному файлі = %d" % self.word_counter)

if __name__ == "__main__":
    file_reader = FileReader("input.txt")


    # Треба підписати усіх слухачів на отримання повідомлень від file_reader
    file_printer = FilePrinter()
    file_reader.registerListener(file_printer)

    word_counter = WordCounter()
    file_reader.registerListener(word_counter)

    file_reader.read()

    word_counter.showResult()