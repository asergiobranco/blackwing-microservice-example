from bwmicroservice import BlackwingHandlerStreamer
from bwmicroservice import BlackwingMicroservice

class MyHandler(BlackwingHandlerStreamer):
    """Create you own handler class, or package.
    """
    def setup(self):
        """Inits the microservice context
        Should only be set if necessary. By default it does nothing.
        """
        self.requests_attended = 0

    def attendRequest(self):
        print("Attending request %d of 20" %(self.requests_attended+1))
        if self.requests_attended == 0:
            # will only run once
            self.first_request()
        else:
            self.response = self.parse_request()

        self.update_count()
        self.verify_if_count_is_20()
    
    def verify_if_count_is_20(self):
        if self.requests_attended == 20:
            print("last request")
            self.keep_alive.value = 0 # tells the handler that it should close the connection
    
    def update_count(self):
        self.requests_attended += 1
    
    def first_request(self):
        self.response = "Welcome, what do you want?"
        
    
    def parse_request(self):
        """
        The self.letter contains the message comming from the client.
        It was already parsed from msgpack to python object.        
        """
        return self.letter 
    
    def clean(self):
        print("I finish all my work")

microservice = BlackwingMicroservice(
    configuration_path="/home/bwmicroservice/msdir/config.yaml", # the yaml configuration file
    handler=MyHandler #the class to use as handler
)

microservice.start() # starts the microservice