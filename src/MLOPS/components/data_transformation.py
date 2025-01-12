import os
from MLOPS import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from MLOPS.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config

        #Different eda operations can be done

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        #splitting data into training and test sets. (0.75, 0.25)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)