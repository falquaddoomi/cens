import sms

class BaseTask(object):
    """base class for tasks"""
    
    def __init__(self, graph=None, interaction=None, currentnode=None, tasknamespace_override=None):
        print 'in Task.__init__():'
        self.interaction = interaction
        self.tasknamespace_override = tasknamespace_override

    def setinteraction(self, graph, initialnode, label):
        self.interaction = sms.Interaction(graph=graph, initialnode=initialnode, label=label)

    
    @staticmethod
    def get_user_init_string():
        return None

    @staticmethod
    def determine_task_type(message):
        return None


        
