import os
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["SERPER_API_KEY"] = "y04a34a8933c895d96c5a637f524992b64c5c24b2"


# Setup the tool for internet searching capabilities
google_search_tool = SerperDevTool()



