import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from typing import Any,List,Dict
import mlflow
from prefect import flow,task

@task
def load_data(path:str,unwanted_cols:Any) -> pd.DataFrame:
    data = pd.read_csv(path)
    data.drop(unwanted_cols,axis=1,inplace=True)
    return data

@task
def get_scaler(data:pd.Series)-> Any:
    scaler = StandardScaler()
    scaler.fit(data)
    return scaler

@task
def rescale_data(data:pd.Series,scaler:Any)->pd.Series:
    data_rescaled = pd.DataFrame(scaler.transform(data),columns=data.columns,index=data.index)
    return data_rescaled

@task
def cut_encoder(cut:pd.Series)->Any:
    cut_ = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Ideal': 4, 'Premium': 5}

    cut_encoded= cut.apply(lambda x: cut_[x])
    return cut_encoded

@task
def clarity_encoder(clarity:pd.Series)->Any:
    clarity_ = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

    clarity_encoded = clarity.apply(lambda x: clarity_[x])
    return clarity_encoded

@task
def color_encoder(color:pd.Series)->Any:
    color_ = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}

    color_encoded = color.apply(lambda x: color_[x])
    return color_encoded

@task
def split_data(input_:pd.DataFrame,output_:pd.Series,test_data_ratio:float)->Dict[str,Any]:
    x_tr,x_te,y_tr,y_te = train_test_split(input_,output_,test_size=test_data_ratio,random_state=42)
    return {'x_train':x_tr,'y_train':y_tr,'x_test':x_te,'y_test':y_te}

@task
def find_best_model(x_train: pd.DataFrame, y_train: pd.Series, estimator: Any, parameters: List) -> Any:
    mlflow.sklearn.autolog(max_tuning_runs=None)

    with mlflow.start_run():
        clf = GridSearchCV(
            estimator=estimator,
            param_grid=parameters,
            scoring='r2',
            cv=5,
            return_train_score=True,
            verbose=1
        )
        clf.fit(x_train, y_train)

        # Disabling autologging
        mlflow.sklearn.autolog(disable=True)

        return clf

#WORKFLOW
@flow
def main(path:str):

    mlflow.set_tracking_uri('sqlite:///mlflow1.db')
    mlflow.set_experiment('diamondprediction')

    DATA_PATH = path
    TARGET_COL = 'price'
    UNWANTED_COLS = ['x','y','z','table','depth']
    TEST_DATA_RATIO = 0.2

    df = load_data(path=DATA_PATH,unwanted_cols = UNWANTED_COLS)
    target_data = df[TARGET_COL]
    input_data = df.drop([TARGET_COL],axis=1)

    train_test_dict = split_data(input_ = input_data,output_=target_data,test_data_ratio=TEST_DATA_RATIO)

    scaler = get_scaler(train_test_dict['x_train'][['carat']])
    train_test_dict['x_train']['carat'] = rescale_data(data=train_test_dict['x_train'][['carat']], scaler=scaler)
    train_test_dict['x_test']['carat'] = rescale_data(data=train_test_dict['x_test'][['carat']], scaler=scaler)
    train_test_dict['x_train']['cut'] = cut_encoder(train_test_dict['x_train']['cut'])
    train_test_dict['x_test']['cut'] = cut_encoder(train_test_dict['x_test']['cut'])
    train_test_dict['x_train']['clarity'] = clarity_encoder(train_test_dict['x_train']['clarity'])
    train_test_dict['x_test']['clarity'] = clarity_encoder(train_test_dict['x_test']['clarity'])
    train_test_dict['x_train']['color'] = color_encoder(train_test_dict['x_train']['color'])
    train_test_dict['x_test']['color'] = color_encoder(train_test_dict['x_test']['color'])

    ESTIMATOR = KNeighborsRegressor()
    HYPERPARAMETERS = [{'n_neighbors': [i for i in range(1, 51)], 'p': [1, 2]}]
    reg = find_best_model(train_test_dict['x_train'], train_test_dict['y_train'], ESTIMATOR, HYPERPARAMETERS)
    print(reg.best_params_)
    print(reg.score(train_test_dict['x_test'], train_test_dict['y_test']))

main(path= r"C:/Users/lokit/Downloads/diamonds.csv")

from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

deployment = Deployment.build_from_flow(
    flow=main,
    name="model_training",
    schedule=IntervalSchedule(interval=timedelta(days=7)),
    work_queue_name="ml"
)

deployment.apply()