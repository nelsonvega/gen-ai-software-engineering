import models as m
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



if __name__=="__main__":
    
    solution=m.SolutionGenerator("Financial","A system that provide tax optimization strategies for traders","output")
    solution.generate()