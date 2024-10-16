import os
import logging
import time
from datetime import datetime


# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='business_idea_generation.log',
                    filemode='w')

logger = logging.getLogger(__name__)

# Also log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.info("Script execution started")


class PatternCatalog:
    def __init__(self) -> None:
        self.PROMPT_PATTERNS = {
            "Problem Identification": "Identify 5 significant problems or pain points in the [INDUSTRY] industry that could be addressed by innovative solutions.",
            "Market Analysis": "Analyze the current market trends and opportunities in the [INDUSTRY] sector. What are the emerging needs and gaps that new businesses could address?",
            "Customer Persona": "Create a detailed customer persona for a potential user of products/services in the [INDUSTRY] industry. Include demographics, behaviors, needs, and pain points.",
            "Solution Brainstorming": "Based on the identified problem in [INDUSTRY], generate 5 innovative business ideas that could effectively address this issue. Provide a brief description for each idea.",
            "Value Proposition": "For the business idea of [BUSINESS_IDEA], craft a compelling value proposition that clearly communicates its unique benefits and differentiators.",
            "Revenue Model": "Propose 3 potential revenue models for the [BUSINESS_IDEA]. Explain how each model would work and its potential advantages.",
            "Competitive Analysis": "Identify and analyze 3 potential competitors for [BUSINESS_IDEA]. What are their strengths and weaknesses, and how could the new business differentiate itself?",
            "Marketing Strategy": "Suggest an initial marketing strategy for [BUSINESS_IDEA]. Include target audience, key messaging, and potential marketing channels.",
            "Resource Requirements": "List the key resources (human, financial, technological) that would be required to launch and operate [BUSINESS_IDEA] successfully.",
            "Scalability Assessment": "Evaluate the scalability potential of [BUSINESS_IDEA]. What factors would facilitate or hinder its growth, and how could it expand into new markets or segments?"
        }
        logger.info(f"Loaded {len(self.PROMPT_PATTERNS)} prompt patterns")

    def generate_content(self,industry = "technology",idea = "AI-powered personal productivity assistant"
    ):
        logger.info("Starting markdown generation")
        markdown_content = f"# Business Idea Generation Session\n\nDate: {datetime.now().strftime('%Y-%m-%d')}\n\n"

        # Placeholder for industry and business idea
        for topic, prompt in self.PROMPT_PATTERNS.items():
            logger.info(f"Processing topic: {topic}")
            formatted_prompt = prompt.replace("[INDUSTRY]", industry).replace("[BUSINESS_IDEA]", idea)
            markdown_content += f"## {topic}\n\n"
            markdown_content += f"**Prompt:** {formatted_prompt}\n\n"
            try:
                response = oai.connect_api(formatted_prompt)
                markdown_content += f"**Response:**\n\n{response}\n\n"
            except Exception as e:
                logger.error(f"Failed to get AI response for topic '{topic}': {str(e)}")
                markdown_content += f"**Response:** Error occurred while fetching response.\n\n"
            markdown_content += "---\n\n"
            logger.info(f"Completed processing for topic: {topic}")

        logger.info("Markdown generation completed")
        return markdown_content

    def save_content(self,content, filename="business_idea_generation.md",topic=""):
        logger.info(f"Saving markdown content to file: {filename}")

        # Format the timestamp to be filename-friendly (without spaces, colons, etc.)
        timestamp = time.strftime('%Y%m%d_%H%M%S')

        topic=topic.replace(' ',"_")
        output="output"
        filename=f'{filename}_{topic}_{timestamp}.md'

        output_path = os.path.join( os.path.join(output,f"{filename}_{timestamp}.md"))
    
    
        os.makedirs(output, exist_ok=True)
        
        
        try:
            with open(output_path, "w") as f:
                f.write(content)
            logger.info(f"Successfully saved markdown file: {filename}")
        except Exception as e:
            logger.error(f"Error saving markdown file: {str(e)}")
            raise
    
    def generate(self,industry:str,topic:str,output_file_name:str):
        content=self.generate_content(industry,topic)
        self.save_content(content,output_file_name,topic)