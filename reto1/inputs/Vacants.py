# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:46:52 2020

@author: USER
"""

# Importar herramientas
import hackaUtils
import pandas as pd

# Importar dataset
dt_Stages = 'Stages'
dt_Vacants = 'Vacants'
dt_Applications = 'Applications'
dt_ApplicationStages = 'ApplicationStages'

datasetStages = hackaUtils.get_dataset([dt_Stages])[dt_Stages]
datasetVacants = hackaUtils.get_dataset([dt_Vacants])[dt_Vacants]
datasetApplications = hackaUtils.get_dataset([dt_Applications])[dt_Applications]
datasetApplicationStages = hackaUtils.get_dataset([dt_ApplicationStages])[dt_ApplicationStages]

groupdataStages = datasetStages.groupby('stage_type', as_index=False).agg({"id": "count"})

dataSetApplications7503 =  datasetApplications.loc[datasetApplications['vacant_id'] == 7503]

stages7503applicants = pd.DataFrame(data = None, columns = datasetApplicationStages.columns)

for application7503 in dataSetApplications7503.values:
    applicationStage7503 = datasetApplicationStages[datasetApplicationStages.application_id==application7503[0]] 
    print(applicationStage7503)
    stages7503applicants = pd.concat([applicationStage7503, stages7503applicants], ignore_index=True, sort=False)

print(stages7503applicants.groupby('stage_id', as_index=False).agg({"id": "count"}))