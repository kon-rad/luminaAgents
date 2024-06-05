from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from luminaagents.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
from crewai_tools import SerperDevTool


@CrewBase
class LuminaagentsCrew():
    """Luminaagents crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def journal_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['journal_analyzer'],
            verbose=True
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            # Example of custom tool, loaded on the beginning of file
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'],
            verbose=True
        )

    @task
    def analyze_journal_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_journal_task'],
            agent=self.journal_analyzer()
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
