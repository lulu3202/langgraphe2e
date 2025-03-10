from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

#insert any number of tools created into this fuction 
def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools

#above tools in the form of node
def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools) #ToolNode is a ready-made building block that helps an AI agent use external tools
#assigning the input argument tools to the tools parameter inside ToolNode
