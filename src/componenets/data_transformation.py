import sys
from dataclasses import dataclass
import os

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline


from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocesor_obj_file_path = os.path.join('artifacts',"preprocesor.pkl")

class DataTranformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_obj(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_col  = ['writing_score','reading_score']
            categorical_col = [
                    "gender",
                    "race_ethnicity",
                   "parental_level_of_education",  
                    "lunch",
                    "test_preparation_course"       
                    
                    ]

            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('oh_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical features standard scaling completed")
            logging.info("Categorical features encoding completed")
            pre_processor = ColumnTransformer(
                [
                    ('num_feature',num_pipeline,numerical_col),
                    ('cat_features',cat_pipeline,categorical_col)
                ]

            )
            return pre_processor
     
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("read train and test done")

            preprocesing_obj = self.get_data_transformation_obj()

            target_col_name = 'math_score'
            numerical_col  = ['writing_score','reading_score']

            input_feature_train_df = train_df.drop(columns=['math_score'],axis=1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(columns=['math_score'],axis=1)
            target_feature_test_df = test_df[target_col_name]

            logging.info("Applying preprocessing object training and test datframe")

            input_feature_train_arr = preprocesing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocesing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]
            logging.info("saved preprocessing object")
            save_object(
                file_path = self.data_transformation_config.preprocesor_obj_file_path,
                obj = preprocesing_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocesor_obj_file_path
                )


        except Exception as e:
            raise CustomException(e,sys)
    

