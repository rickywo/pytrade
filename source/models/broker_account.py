from abc import ABCMeta


class BrokerAccount:
    __metaclass__ = ABCMeta
    __accountId = None
    __password = None

    def setPassword(self, raw_password):
        # TODO: To encrypt raw password
        pass

    # Use the passphrase of an user if logged in successfully
    def getPassword(self, passphrase):
        pass
