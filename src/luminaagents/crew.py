from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import EXASearchTool

# Initialize the tool for internet searching capabilities
tool = EXASearchTool()
# Uncomment the following line to use an example of a custom tool
# from luminaagents.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
# Agent(
#     # ...
#     llm=self.groq_llm
# )


@CrewBase
class LuminaagentsCrew():
    """Luminaagents crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    groq_llm = ChatGroq(temperature=0.7, model_name="llama3-70b-8192")

    @agent
    def journal_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['journal_analyzer'],
            verbose=True,
            llm=self.groq_llm
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            # Example of custom tool, loaded on the beginning of file
            tools=[EXASearchTool()],
            verbose=True,
            llm=self.groq_llm
        )

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'],
            verbose=True,
            llm=self.groq_llm
        )

    @task
    def analyze_journal_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_journal_task'],
            agent=self.journal_analyzer(),
            llm=self.groq_llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def compile_actions_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_actions_task'],
            agent=self.planner(),
            output_file='next_actions.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SelfDevelopment crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
