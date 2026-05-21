# import sys
# from visa.logger import logging
# from visa.exception import USvisaException

# try:
#     a = 1 / 0
# except Exception as e:
#     raise USvisaException(e, sys)
from dotenv import load_dotenv
load_dotenv()
from visa.pipeline.training_pipeline import TrainingPipeline
pipeline= TrainingPipeline()
pipeline.run_pipeline()