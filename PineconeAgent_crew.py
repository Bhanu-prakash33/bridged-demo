from crewai import Agent, Crew, Task, Process, LLM
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class PineconeAgentCrew:
    """ A crew for converting Natural language queries into structured Pinecone Vector search queries"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml' 

    def __init__(self):
        
        self.llm = LLM(
            model = 'ollama/mistral:7b',
            base_url = "http://localhost:11434"
        )

    @agent
    def pinequerygen_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['pinequerygen_agent'],
            llm = self.llm 
        )
    
    @task
    def pinecone_agent_task(self) -> Task:
        return Task(
            config = self.tasks_config['pinecone_agent_task'],
        )
    
    @crew # Defining AI Workflow using CrewAI
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents, # Assigns all dynamically created agents
            tasks = self.tasks,
            process = Process.sequential
        )