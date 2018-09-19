__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'


class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtil:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, str):
        self.content += str

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer):
        writer.undo(self.obj)


if __name__ == '__main__':
    caretaker = FileWriterCaretaker()

    writer = FileWriterUtil("data.txt")
    writer.write("First Set of Data\n")
    print(writer.content + "\n\n")

    # lets save the file
    caretaker.save(writer)
    # now write something else
    writer.write("Second Set of Data\n")

    # checking file contents
    print(writer.content + "\n\n")

    # lets undo to last save
    caretaker.undo(writer)

    # checking file content again
    print(writer.content + "\n\n")
