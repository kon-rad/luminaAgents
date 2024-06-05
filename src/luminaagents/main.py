#!/usr/bin/env python
import agentops
from luminaagents.crew import LuminaagentsCrew
import os

agentOpsKey = os.getenv("AGENTOPS_API_KEY")
agentops.init(agentOpsKey)


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'journal': "this is a sample journal, I need to win this hackathon and make 10K MRR"
    }
    LuminaagentsCrew().crew().kickoff(inputs=inputs)
