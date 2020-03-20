import hackaUtils
import pandas as pd


# Importar datasets
#%%
dt_name = 'Applications'
application_dataset = hackaUtils.get_dataset([dt_name])[dt_name]


#%%
dt_name = 'ApplicationStages'
application_stages_dataset = hackaUtils.get_dataset([dt_name])[dt_name]


#%%
dt_name = 'Stages'
stages_dataset = hackaUtils.get_dataset([dt_name])[dt_name]



#%%


#%%



#%% Esqueleto del dataset final

# Cargar dataset filtrado de candidatos y de vacantes
candidates_dataset = pd.read_csv('filtered_candidates.csv')
vacants_dataset = pd.read_csv('filtered_vacants.csv')

candidates_columns = candidates_dataset.keys().to_list()
candidates_columns.pop(0)

for index in range(0,len(candidates_columns)):
    candidates_columns[index] = 'c-' + candidates_columns[index]
    


vacants_columns = vacants_dataset.keys().to_list()
vacants_columns.pop(0)

for index in range(0,len(vacants_columns)):
    vacants_columns[index] = 'v-' + vacants_columns[index]
    

columns = candidates_columns + vacants_columns
columns.append('ascended')
final_dt = pd.DataFrame(columns=columns)

#%%
# Procedimiento --> Poblar dataset

#%% 1. De application se saca el id de la vacante y el id del candidato y de application
from datetime import datetime
cont = 0
empty = 0
for index, row in application_dataset.iterrows():
    
    #1. De application se saca el id de la vacante y el id del candidato y de application
    application_id = row['id']
    vacant_id = row['vacant_id']
    candidate_id = row['candidate_id']
    
    #2. Con el id de application, se busca en applicationStage el id de las stages por application
    stages = application_stages_dataset.loc[application_stages_dataset["application_id"] == application_id]
    #print(stages)
    
    
    previous_date = datetime.utcfromtimestamp(318312000)
    last_stage = None
    #stage_status_cond = False
    #stage_type_cond = False
    ascension = False
    stage_id = None
    for stage_index, stage_row in stages.iterrows():
        
        
        #3. Si el stage_type es 0 o 1 y en applicationStage está el status en 'active' o 'accepted'
        # se agrega la vacante y el candidato a la clase '1' que sería ascendió
        # hay que mirar el stage más reciente, debe ser accepted o active
        
        datetime_str = stage_row['created_at'][:-4]
        current_stage_date = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        
        if(current_stage_date > previous_date):
            last_stage = current_stage_date
            stage_status = stage_row['status']
            stage_id = stage_row['stage_id']
            
            # Esto no será necesario
            #if(stage_status == 'accepted' or stage_status == 'active'):
            #    stage_status_cond = True
            #else:
            #    stage_status_cond = False
                
        previous_stage = current_stage_date
        
    
    
    stage_type = stages_dataset.loc[stages_dataset['id'] == stage_id]
    stage_type = stage_type['stage_type'].to_list()
    
    if(len(stage_type) == 0):
        # Si no hay referencia al stage, no se tiene en cuenta esa aplicación
        empty += 1
        
    else:
        # Escenarios en que asciende:
        # stage_type = 0,1   &&   stage_status == 'accepted'
        # stage_type > 1     &&   stage_status == 'accepted' o 'active'
        # Si no cumple con esas condiciones, no asciende
        
        stage_type = stage_type[0]
        if(stage_type in [0,1] and stage_status == 'accepted'):
            ascension = True
        elif(stage_type > 1 and stage_status in ['active','accepted']):
            ascension = True
        else:
            ascension = False
            
        
        # Insertar en dataset definitivo
        # Hacen falta registros de candidatos y de vacantes, hay que filtrar
        candidate_data = candidates_dataset.loc[candidates_dataset['id'] == candidate_id]
        vacant_data = vacants_dataset.loc[vacants_dataset['id'] == vacant_id]
        
        #c = candidate_data.to_list()
        #v = vacant_data.to_list()
        #print("\nCANDIDATE")
        #print(candidate_data)
        
        #print("\nVACANT")
        #print(vacant_data)
        
        if(not candidate_data.empty and not vacant_data.empty):
            help_dic = {}
    
            for key in final_dt.keys():
                
                split = key.split('-')
                if(split[0] == 'c'):
                    help_dic[key] = candidate_data[split[1]].to_list()[0]
                    #print(candidate_data[split[1]])
                    
                elif(split[0] == 'v'):
                    help_dic[key] = vacant_data[split[1]].to_list()[0]
                    #print(vacant_data[split[1]])
                    
            if(ascension):
                help_dic['ascended'] = 1
            else:
                help_dic['ascended'] = 0
            
            #a_row = pd.Series(help_dic)
            final_dt = final_dt.append(help_dic, ignore_index = True)
            print(help_dic)
        
            
    
    
    # Controlar cantidad de iteraciones
    cont+=1
    if(cont==10):
        break




#%% 2. Con el id de application, se busca en applicationStage el id de las stages por application


# 3. Si el stage_type es 0 o 1 y en applicationStage está el status en 'active' o 'accepted'
# se agrega la vacante y el candidato a la clase '1' que sería ascendió


# 4. Si no se cumple  con la condición 3, el candidato y la vacante van al 
# la clase '0', que sería equivalente a que no ascendió



