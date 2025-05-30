from PineconeAgent_crew import PineconeAgentCrew 

pineconeAgent_crew = PineconeAgentCrew() 

dataset = [
    {"query" : "Show me articles by Alice Zhang from last year about machine learning."},
    {"query" : "Find posts tagged with ‘LLMs’ published in June, 2023."},
    {"query" : "Anything by John Doe on vector search?"}
]

result = pineconeAgent_crew.crew().kickoff_for_each(inputs = dataset)
