import logging
import services.openaiapi as oai
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Set your OpenAI API key

def generate_multi_agent_architecture(saas_idea: str,output_dir="output") -> dict:
    """
    Generates a multi-agent architecture for a given SaaS idea using an LLM.

    Args:
        saas_idea: A brief description of the SaaS idea.

    Returns:
        A dictionary containing the generated multi-agent architecture, including:
            - queries
            - agents
            - plans_and_skills
            - orchestration
    """

    # 1. Generate Queries
    
    queries_prompt=f"""
    Based on the SaaS idea '{saas_idea}', what are 10 common user queries that the system would need to handle?
    use te following criteria to define the queries of a multi-agent architecture:
    1. Relevance: The query should be relevant to the system's purpose and goals[1][2].

    2. Specificity: Queries should be specific enough to elicit targeted responses from agents[3].

    3. Scope: Define the scope of information or actions requested from agents[4].

    4. Agent roles: Consider which agents or agent types should handle the query based on their roles and capabilities[5][6].

    5. Time constraints: Specify any time limits or deadlines for query responses[7].

    6. Priority: Indicate the relative importance or urgency of the query[8].

    7. Resource requirements: Define computational or data resources needed to process the query[9].

    8. Coordination needs: Specify if coordination between multiple agents is required to answer the query[10][11].

    9. Privacy/security: Consider data privacy and security requirements in formulating the query[6][12].

    10. Query language: Use a standardized query language or format understood by all agents[13].

    11. Context: Provide relevant contextual information to help agents interpret and respond to the query[14].

    12. Expected output: Clearly define the expected format and content of query responses[15].

    13. Failure handling: Specify how to handle partial or failed responses from agents.

    14. Scalability: Ensure queries can scale as the number of agents in the system grows.

    15. Adaptability: Allow for dynamic adjustment of queries based on changing system conditions.

    16. Learning capability: Enable agents to learn from and improve their responses to recurring query types.

    17. Conflict resolution: Define how to resolve conflicting responses from multiple agents.

    18. Feedback mechanism: Include a way for agents to provide feedback on query quality or results.

    19. Ontology alignment: Ensure consistent understanding of concepts across agents with different knowledge bases.

    20. Performance metrics: Define metrics to evaluate the efficiency and effectiveness of query processing.
    
    
    """
    queries = oai.connect_api(prompt=queries_prompt).split('\n')

    # 2. Generate Agents
    
    agents_prompt=f"""
        Based on the SaaS idea '{saas_idea}', what are 5 agents that could be used to build a multi-agent architecture?
        
        Use te following criteria to define the agents in a multi-agent architecture

        1. **Autonomy**: Agents should be able to operate independently and make decisions without constant external intervention[1][2].

        2. **Reactivity**: Agents must be able to perceive and respond to changes in their environment in a timely manner[1][2].

        3. **Proactivity**: Agents should exhibit goal-directed behavior, taking initiative to achieve objectives rather than simply reacting to stimuli[1][2].

        4. **Social Ability**: Agents must be capable of interacting and communicating with other agents and possibly humans[1][2].

        ## Cognitive Capabilities

        5. **Deliberativity**: Agents should be able to reason about their actions, considering both environmental information and past experiences[2].

        6. **Learning**: Agents should have the ability to learn from their experiences and improve their performance over time[4].

        7. **Problem-Solving**: Agents must be equipped with mechanisms to analyze and solve complex problems within their domain[4].

        8. **Decision-Making**: Agents should have robust decision-making capabilities, weighing options and selecting optimal actions[4].

        ## Specialization and Roles

        9. **Specialization**: Agents should have clearly defined roles and areas of expertise within the system[4][5].

        10. **Task Focus**: Each agent should be designed to excel at specific tasks or functions[4][5].

        11. **Complementary Skills**: The collective abilities of agents should cover all required system functionalities[4][5].

        ## Communication and Interaction

        12. **Communication Protocol**: Agents must adhere to standardized communication protocols for effective interaction[6].

        13. **Information Sharing**: Agents should be able to exchange relevant information with other agents in the system[6].

        14. **Negotiation Skills**: Agents must be capable of negotiating with other agents to resolve conflicts and allocate resources[6].

        ## Adaptability and Flexibility

        15. **Environmental Awareness**: Agents should maintain an up-to-date model of their environment[1][2].

        16. **Adaptability**: Agents must be able to adjust their behavior based on changing circumstances[4].

        17. **Scalability**: The agent architecture should allow for easy addition or removal of agents without disrupting the system[4].

        ## System Integration

        18. **Interoperability**: Agents should be designed to work seamlessly with other agents and external systems[5].

        19. **Resource Management**: Agents must be able to manage their own resources efficiently and coordinate resource usage with other agents[5].

        20. **Goal Alignment**: Individual agent goals should align with and contribute to the overall system objectives[5].

        
        """
    agents = oai.connect_api(prompt=agents_prompt).split("\n")

    # 3. Generate Plans and Skills
    plans_and_skills = {}
    for agent in agents:
       agent_prompt=f"""For the agent '{agent}', what are its 3 main plans and 3 core skills?
       Use the following criteria to define the plans and skills of an agent in a multi-agent architecture:
       
        ## Agent Specialization

        **Domain expertise:** Each agent should have clearly defined areas of expertise or specialization[1][5]. For example, in a data analysis system, you may have agents specialized in:

        - Data retrieval and presentation
        - Deep analysis and insight generation 
        - Planning and decision-making

        **Skill set:** Define the specific skills and capabilities each agent possesses within its domain[2]. This could include:

        - Natural language processing
        - Mathematical modeling
        - Visual recognition
        - Logical reasoning

        ## Task Decomposition

        **Subtask identification:** Break down complex goals into smaller, manageable subtasks that can be assigned to individual agents[1][4].

        **Interdependencies:** Map out how subtasks relate to each other and the overall objective[1]. This helps in:

        - Determining task sequencing
        - Identifying parallel processes
        - Managing information flow between agents

        ## Planning Capabilities

        **Planning approaches:** Specify the planning methods each agent can employ[7], such as:

        - Task decomposition
        - Multi-plan selection
        - Reflection and refinement
        - Memory-augmented planning

        **Adaptability:** Define how agents can adjust their plans based on new information or changing circumstances[5].

        ## Communication Protocols

        **Interaction methods:** Establish how agents will communicate and share information[2][3]. This may include:

        - Direct agent-to-agent messaging
        - Shared environment modifications
        - Centralized information hubs

        **Information sharing:** Define what types of data and insights agents can exchange, such as:

        - Sensor readings
        - Learned policies
        - Real-time experiences

        ## Tool Integration

        **Available tools:** Specify the external tools and resources each agent can access and utilize[1][7]. These might include:

        - Databases
        - APIs
        - Specialized software
        - Sensory equipment

        **Tool proficiency:** Define the agent's level of expertise in using each tool and any constraints on tool usage.

        ## Performance Metrics

        **Evaluation criteria:** Establish metrics to assess each agent's performance[4], such as:

        - Task completion rate
        - Accuracy of outputs
        - Processing speed
        - Resource utilization

        **Collaborative efficiency:** Measure how well agents work together towards common goals[3].

        ## Learning and Adaptation

        **Learning mechanisms:** Define how agents can improve their skills and knowledge over time[2]. This may involve:

        - Reinforcement learning
        - Transfer learning from other agents
        - Feedback incorporation

        **Knowledge sharing:** Specify how agents can transfer learned information to enhance overall system performance[2].

        ## Ethical and Safety Constraints

        **Operational boundaries:** Clearly define the ethical and safety limits within which agents must operate[3].

        **Fail-safe behaviors:** Establish protocols for handling unexpected situations or potential failures[3].

        By carefully considering these criteria, you can create a robust framework for defining agent plans and skills within a multi-agent system. This approach ensures that each agent has a clear role, appropriate capabilities, and the necessary tools to contribute effectively to the overall system goals.
       
       """

       response = oai.connect_api(prompt=agent_prompt)
       plans_and_skills[agent] = {
            "plans": response.split("\n")[0:3],
            "skills": response.split("\n")[3:6]
        }

    # 4. Generate Orchestration
    
    orchestrator_prompt=f"""Based on the SaaS idea '{saas_idea}' and the agents you generated, describe the orchestration process for handling user queries.
    
    Use the following criteria to define the orchestration process in a multi-agent architecture:
    
    
    ## Core Criteria for Multi-Agent Orchestration

        ### Task Decomposition and Assignment
        
        **Task Analysis**: The orchestrator must be able to break down complex tasks into smaller, manageable subtasks[1]. This involves:
        - Identifying the required properties of each subtask
        - Determining the expertise needed for each component
        
        **Agent Matching**: Assign subtasks to agents based on their specialized capabilities and current workload[1]. This ensures:
        - Efficient resource allocation
        - Utilization of each agent's strengths
        
        ### Communication and Coordination
        
        **Standardized Protocols**: Implement communication protocols that allow seamless interaction between agents, regardless of their underlying technologies[1]. This facilitates:
        - Clear information exchange
        - Consistent message formatting
        
        **Feedback Mechanisms**: Establish continuous feedback loops to enable real-time adaptation of workflows[1]. This allows:
        - Agents to adjust actions based on outcomes
        - Dynamic optimization of the orchestration process
        
        ### Scalability and Flexibility
        
        **Modular Design**: The orchestration system should be modular, allowing for easy integration of new agents and functionalities without disrupting existing workflows[1]. This promotes:
        - System expandability
        - Adaptability to changing requirements
        
        **Dynamic Resource Allocation**: Implement mechanisms to scale resources efficiently as task complexity increases[1]. This ensures:
        - Consistent performance under varying loads
        - Optimal utilization of available agents
        
        ### Context Management
        
        **Global Context Awareness**: The orchestrator should maintain a comprehensive view of all agent conversations and task histories[3]. This enables:
        - Intelligent routing of requests
        - Maintenance of context across multiple interactions
        
        **Agent-Specific Context**: Individual agents should have access to their own conversation histories, allowing for continuity in their specific tasks[3].
        
        ### Interoperability
        
        **Platform Independence**: Design the orchestration system to work across different platforms and technologies[1]. This allows for:
        - Integration of diverse AI models and tools
        - Flexibility in agent selection and deployment
        
        ### Decision-Making and Conflict Resolution
        
        **Intelligent Routing**: Implement a classification system that can analyze user requests, agent descriptions, and conversation histories to determine the most appropriate agent for each task[3].
        
        **Conflict Management**: Develop mechanisms to resolve conflicts that may arise when multiple agents attempt to access shared resources or data[4].
        
        ### Security and Data Management
        
        **Secure Communication**: Implement robust security measures to safeguard data exchange between agents and protect against unauthorized access[4].
        
        **Efficient Data Handling**: Utilize data management systems that allow agents to quickly access and share information[1].
        
        ### Performance Monitoring and Optimization
        
        **Metrics Tracking**: Implement systems to monitor key performance indicators of the orchestration process[4]. This includes:
        - Task completion rates
        - Resource utilization
        - Response times
        
        **Continuous Improvement**: Use gathered data to optimize the orchestration process over time, refining agent assignments and workflow patterns.
        
        ## Implementation Considerations
        
        When implementing these criteria, consider the following:
        
        1. Use AI frameworks that support multi-agent orchestration, such as AutoGPT or BabyAGI[1].
        
        2. Leverage cloud-based solutions for scalability and flexibility[4].
        
        3. Implement a centralized orchestrator component to manage the overall process flow and agent interactions[3].
        
        4. Design clear agent descriptions and roles to facilitate accurate task assignment[3].
        
        5. Develop fallback mechanisms and error handling procedures to ensure system resilience[3].

                            
    
    """
    
    orchestration = oai.connect_api(prompt=orchestrator_prompt).split("\n")
    
    return {
        "queries": queries,
        "agents": agents,
        "plans_and_skills": plans_and_skills,
        "orchestration": orchestration
    }

def generate_solution(saas_idea: str,output="output") -> str:
    """
Generates Marp Markdown for the multi-agent architecture.

Args:
    saas_idea: The SaaS idea.

Returns:
    Marp Markdown string.
"""

    architecture = generate_multi_agent_architecture(saas_idea)

    markdown = f"""---
marp : true
theme : gaia
---

# Multi-Agent Architecture for {saas_idea}

---

## Queries to Handle

    """
    markdown += "\n"
    for query in architecture["queries"]:
        markdown += f"{query.strip()}\n"

    markdown += """

---

## Agents Needed

"""
    i=0
    for agent in architecture["agents"]:
        markdown += f"{agent.strip()}\n"
    markdown += """

---

## Plans and Skills:

"""
    for agent, data in architecture["plans_and_skills"].items():
        markdown += f"{agent.strip()} \n"
        markdown += f"**Plans:**\n"
        for plan in data["plans"]:
            markdown += f" {plan.strip()}\n"
        markdown += f"**Skills:**\n"
        for skill in data["skills"]:
            markdown += f" {skill.strip()}\n"

    markdown += """

---

## Orchestration Operation

"""

    #markdown += architecture["orchestration"].strip()
    for orch in architecture["orchestration"]:
        markdown += f"{orch.strip()}\n"
        

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    
    output_path = os.path.join( os.path.join(output,f"ma_architecture_{timestamp}.md"))
    
    
    os.makedirs(output, exist_ok=True)
    with open(output_path, 'w') as file:
        file.write(markdown)

    
    return markdown


if __name__ == "__main__":  
    
    saas_idea = "A system that provide tax optimization strategies for traders"
    
    marp_markdown = generate_marp_markdown(saas_idea,output_dir="output")
   

    print("Marp Markdown generated in multi_agent_architecture.md")
