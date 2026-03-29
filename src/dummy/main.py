#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from dummy.crew import dummy


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI agents in Coding',
        'current_year': str(datetime.now().year)
    }

    try:
        dummy().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

