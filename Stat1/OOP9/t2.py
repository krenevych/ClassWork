from abc import ABCMeta, abstractmethod


class FileReaderListener(metaclass=ABCMeta):
    """інтерфейс Спостерігач отримання рядків файлу."""
    @abstractmethod
    def onReceive(self, line: str):
        pass


class FileReader:

    def __init__(self, fname):
        self.__fname = fname
        self.__listeners = set()

    def registerListener(self, listener):
        self.__listeners.add(listener)

    def __notyfyListeners(self, line):
        "Повідомити усіх слухачів, що підписалися"
        for listener in self.__listeners:
            # повідомити listener про прочинатий новий рядок
            listener.onReceive(line)

    def read(self):
        with open(self.__fname) as f:
            for line in f:
                self.__notyfyListeners(line)


class FileLinePrinter(FileReaderListener):
    def onReceive(self, line):
        print(line)

class WordCounter(FileReaderListener):
    def __init__(self):
        self.__wordcounter = 0

    def onReceive(self, line):
        words = line.split()
        self.__wordcounter += len(words)

    def result(self):
        print("Кількість слів у файлі:", self.__wordcounter)

if __name__ == "__main__":
    reader = FileReader("t1.py")


    # Підписка слухачів
    reader.registerListener(FileLinePrinter())

    wordCounter = WordCounter()
    reader.registerListener(wordCounter)
    # Всі слухачі підписалися

    reader.read()

    wordCounter.result()



