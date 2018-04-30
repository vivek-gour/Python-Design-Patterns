__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class CommandExecutor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def runCommand(self, cmd):
        pass


class CommandExecutorImpl(CommandExecutor):
    def runCommand(self, cmd):
        print("{0} command executed.".format(cmd))


class CommandExecutorProxy(CommandExecutor):
    def __init__(self, user, pwd):
        self.is_admin = False
        if "Admin" == user and "qwerty" == pwd:
            self.is_admin = True
        self.executor = CommandExecutorImpl()

    def runCommand(self, cmd):
        if self.is_admin:
            self.executor.runCommand(cmd)
        else:
            if cmd.strip().startswith("rm"):
                raise Exception("rm command is not allowed for non-admin users.")
            else:
                self.executor.runCommand(cmd)


if __name__ == '__main__':
    executor = CommandExecutorProxy("Admin", "123456")
    try:
        executor.runCommand("ls -ltr")
        executor.runCommand("rm -rf abc.pdf")
    except Exception as e:
        print(e)
