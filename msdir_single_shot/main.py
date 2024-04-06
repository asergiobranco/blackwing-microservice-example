from bwmicroservice import BlackwingHandler
from bwmicroservice import BlackwingMicroservice

class MyHandler(BlackwingHandler):
    """Create you own handler class, or package.
    """
    def setup(self):
        """Inits the microservice context
        Should only be set if necessary. By default it does nothing.
        """
        self.variable_to_init = 10

    def attendRequest(self):
        # The self.response will carry the message to the client
        # no serialization is necessary
        self.response = self.parse_request()
        # AFTER THIS LINE THE CONNECTION WILL BE CLOSED!
        
    
    def parse_request(self):
        """
        The self.letter contains the message comming from the client.
        It was already parsed from msgpack to python object.        
        """
        print(self.letter)
        if self.letter == b'Hello World':
            return "How are you?"
        else:
            return "Goodbye"

microservice = BlackwingMicroservice(
    configuration_path="/home/bwmicroservice/msdir/config.yaml", # the yaml configuration file
    handler=MyHandler #the class to use as handler
)

microservice.start() # starts the microservice