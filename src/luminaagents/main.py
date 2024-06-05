#!/usr/bin/env python
from luminaagents.crew import LuminaagentsCrew

import agentops
agentops.init()


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'journal': "Today, I spent a lot of time thinking about my career and personal goals. I've been feeling somewhat stuck in my current job, and I'm not sure if it's where I want to be in the long term. I've always been passionate about writing and storytelling, but I've never pursued it seriously. Recently, I came across a few articles about freelance writing and the opportunities it offers, which got me thinking about giving it a try."
    }
    LuminaagentsCrew().crew().kickoff(inputs=inputs)
