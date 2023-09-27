# UNC Charlotte
# ITCS 5153 - Applied AI - Fall 2023
# Lab 1
# A test of the AIMA book code
# Student ID: 800908508

from agents import TrivialVacuumEnvironment, ReflexVacuumAgent, TableDrivenVacuumAgent, RandomVacuumAgent, ModelBasedVacuumAgent 

#print("Hello world!")

#loc_A, loc_B = (0, 0), (1, 0)  # The two locations for the Vacuum world

#def ReflexVacuumAgent():
#    """
#    [Figure 2.8]
#    A reflex agent for the two-state vacuum environment.
#    >>> agent = ReflexVacuumAgent()
#    >>> environment = TrivialVacuumEnvironment()
#    >>> environment.add_thing(agent)
#    >>> environment.run()
#    >>> environment.status == {(1,0):'Clean' , (0,0) : 'Clean'}
#    True
#    """
#
#    def program(percept):
#        location, status = percept
#        if status == 'Dirty':
#            return 'Suck'
#        elif location == loc_A:
#            return 'Right'
#        elif location == loc_B:
#            return 'Left'
#
#    return Agent(program)
#
#
#print(ReflexVacuumAgent())

def AgentTest(func, text, num):
    # This will create an agent based on input and put it in a TrivialVacuumEnvironment. It will display a before and after status and give its performance rating.
    print('Test', num, '- Creating environment...')
    agent = func
    environment = TrivialVacuumEnvironment()
    environment.status = {(1,0):'Dirty' , (0,0) : 'Dirty'} # make it dirty to match whats on the lab instructions and make it fair
    print(environment.status, '\n')
    environment.add_thing(agent)
    environment.run()
    print('Running', text, 'agent...')
    print(environment.status)
    print('Agent performance:', agent.performance)
    print('________________________________________________________________________________', '\n')


print('\n', '________________________________________________________________________________', '\n')
AgentTest(ReflexVacuumAgent(), 'ReflexVacuumAgent', '1')
AgentTest(TableDrivenVacuumAgent(), 'TableDrivenVacuumAgent', '2')
AgentTest(RandomVacuumAgent(), 'RandomVacuumAgent', '3')
AgentTest(ModelBasedVacuumAgent(), 'ModelBasedVacuumAgent', '4')