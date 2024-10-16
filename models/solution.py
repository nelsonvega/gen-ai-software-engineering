import sys
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import engine as sd

class SolutionGenerator:
    def __init__(self, industry:str,idea:str,output_dir:str):
        self.industry = industry
        self.idea = idea
        self.prompt = self.idea
        self.output_dir = output_dir
        
    def generate_pattern_catalog(self):
        sd.promptcatalog.PatternCatalog().generate(self.industry,self.idea,self.output_dir)
    def generate_solution_design(self):
        sd.solutiondesign.genma.generate_solution(self.idea,self.output_dir)
        
    
    def generate(self):
        self.generate_pattern_catalog()  
        self.generate_solution_design()  
