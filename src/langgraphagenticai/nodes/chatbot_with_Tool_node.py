from src.langgraphagenticai.state.state import State

#State is like a memory that stores chat messages
#creates a chatbot that can Take user messages as input, Use an AI model (llm) to generate responses and Integrate tools to improve its responses

#This class manages a chatbot that can use tools
class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
 #constructor method that takes self (the instance of the class) and model (a parameter)
    def __init__(self,model):
        self.llm = model # Attribute (self.llm) stores the parameter (model)

  #This method processes user input and generates responses. Methods always have self as the first parameter
    def process(self, state: State) -> dict: #-> dict is a return type hint and state:State is also a type hint, expects state to be of type State
        """
        Processes the input state and generates a response with tool integration.
        """
        user_input = state["messages"][-1] if state["messages"] else "" #gets the latest user message from state else nothing
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}]) #AI model (self.llm) generates a response based on user input

        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    
    #This function adds tools to the chatbot.
    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools) #connects the chatbot to external tools
        
        #function that processes messages
        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node
 
        
 
    
    
    
    
    