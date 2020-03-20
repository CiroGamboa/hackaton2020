"""
Descripcion del archivo:
    En este archivo se encuentran metodos de apoyo para la resolucion del reto 1.
    La idea es que en jupyter se puedan visualizar facilmente los analisis y el 
    codigo detallado se encuentre aqui.

Hackaton 2020
Reto 1:
Porcentaje de afinidad: Candidato vs Vacante
Magneto empleos es una plataforma que permite a personas de todos los sectores laborales encontrar
empleos a nivel nacional e internacional y actualmente cuenta con una bolsa de candidatos disponibles
para que grandes empresas encuentren los mejores perfiles que se ajusten a sus vacantes.
 
Esta bolsa de candidatos ha ido creciendo de manera exponencial durante los últimos tiempos. 
Para cada candidato recopilamos desde información personal como: nombres, apellidos, email, teléfonos,
 entre otros, hasta información relevante para el proceso de reclutamiento como los estudios, 
 habilidades personales, experiencia y perfil laboral. Aunque toda esta información es posible 
 llenarla por cada candidato, es permitido ingresar en Magneto Empleos candidatos con tan solo el 
 nombre y el correo electrónico y de manera fácil importarlos a una vacante específica.
 
Esto lleva a que tanto los candidatos con información acorde a la vacante, como candidatos con la 
información incompleta y los candidatos con información poco relevante para la vacante en particular, 
se vean de la misma manera y mezclados entre sí, lo que hace que la búsqueda de perfiles que se 
ajusten con la vacante sean una tarea larga, dispendiosa y costosa.
"""
#%% Se importan las librerias
import pandas as pd


#%% 
def get_dataset(specific_datasets):

    datasets = {'Candidates'         : ['id','email','first_name','last_name','phone','birthdate','gender','identification_type','identification_number','country_birth','city','education_level','salary','profile_description','without_experience','without_studies','title_or_profession','available_to_move','civil_status','has_video','studies','experiences','psy_tests'],
                'Vacants'            : ['id','title','description','salary_type','min_salary','max_salary','status','created_at','company','education_level','agree','requirements','publish_date','confidential','expiration_date','experience_and_positions','knowledge_and_skills','titles_and_studies','number_of_quotas'],
                'Stages'             : ['id','title','send_sms','send_email','send_call','stage_type','vacant_id','stage_oder'],
                'Applications'       : ['id','vacant_id','candidate_id','created_at','status','discard_type'],
                'ApplicationStages'  : ['id','application_id','stage_id','created_at','status']
               }

    out_datasets = {}
    if(len(specific_datasets) == 0):
        for dataset_name in datasets:
            dt = _process_csv_dataset(dataset_name, datasets[dataset_name])
            out_datasets[dataset_name] = dt
    else:
        for dataset_name in specific_datasets:
            dt = _process_csv_dataset(dataset_name, datasets[dataset_name])
            out_datasets[dataset_name] = dt

    return out_datasets  
            
def _process_csv_dataset(dataset_name, dataset_columns):
    dt_folder = 'datasets/'
    dt = pd.read_csv(dt_folder + dataset_name + '.csv')
    dt.columns = dataset_columns
    return dt

def count_empty_records(dataset):
    '''
    Contar cuantos registros estan en NaN por cada campo o son listas vacias
    '''
    total_records = dataset.shape[0]
    print("\t\tMissing data per field")
    print("Total records\t\t", total_records)
    print("Missing data\t\t% of total\tField name(" + str(dataset.shape[1]) + ")")
    nulos =  dataset.isnull().sum()
    
    sorted_nulls = sorted(nulos.items(), key=lambda x: x[1])
    
    # Reverse a las malas
    size = len(sorted_nulls)
    for i in range(size-1,0,-1):
        print(str(sorted_nulls[i][1]) + "\t\t\t" + str(round(sorted_nulls[i][1]*100/total_records)) + "%" + "\t\t" + sorted_nulls[i][0])
    
    #for item in sorted_nulls:
     #   print(str(item[1]) + "\t\t\t" + str(round(item[1]*100/total_records)) + "%" + "\t\t" + item[0])


#%%
def drop_columns(dataset, columns):
    dt = dataset.copy()
    dt.drop(columns=columns, axis=1, inplace=True)       
    return dt



#%%
def count_empty_lists(dataset):
    print("Empty lists")
    total_records = dataset.shape[0]
    print("Total records\t\t", total_records)
    print("Missing data\t\t% of total\tField name(" + str(dataset.shape[1]) + ")")
    for (columnName, columnData) in dataset.iteritems():
        line = ""
        #add = ""
        count  = 0
        for value in columnData.values:
            if(value == '[]'):
                count += 1

        line = str(count)
        line += '\t\t\t' + str(round(count*100/total_records)) + '%'
        line += '\t\t' +  columnName
        print(line)
            

#%% 
def generate_hist(dataset, field):
    dataset.hist(column = field)

#%%
def count_record_per_class(dataset, field):
    '''
    Cuenta cuantos registros hay por clase en cada campo, retorna la lista
    que indica cuantos valores hay por clase
    '''
    print("\n\nField values (%): ",field)
    print(dataset[field].value_counts(normalize=True, dropna=False))
    
    print("\nField values (value): ",field)
    props = dataset[field].value_counts(normalize=False, dropna=False)
    print(props)
    return props
    

#%%
def get_minor_classes(props, position):
    '''
    Obtener las clases de los valores menos dominantes por campo,
    a partir de un indice
    '''
    classes = []
    for index in range(position, len(props)):
        class_value = props.index[index]
        if(pd.isnull(class_value)):
            classes.append(None)
        else:
            classes.append(props.index[index])
    
    return classes

#%%
def replace_minority_values(dataset, field, classes, new_class):
    '''
    Reemplaza los valores en clases minoritarias, por una clase general
    '''

    for index in range(0,dataset.shape[0]):
        value = dataset[field][index]
        if(value in classes):
            dataset.at[index, field] = new_class
        elif(None in classes):
            if(pd.isnull(value)):
                dataset.at[index, field] = new_class
            
#%%
def replace_nan(dataset, field, nan_class):

    '''
    Esto funciona
    
    for index in range(0,dataset.shape[0]):
        value = dataset[field][index]
        if(pd.isnull(value)):
            dataset.at[index, field] = new_class    
    '''
    dataset[field].fillna(nan_class, inplace=True)
    #dataset.loc[pd.isnull(dataset[field])] = new_class

    
#%%
def replace_empty_lists(dataset, field, new_class):
    
    '''
    Esto funciona
    
    for index in range(0,dataset.shape[0]):
        value = dataset[field][index]
        if(value == '[]'):
            dataset.at[index, field] = new_class    
    '''
    
    dataset.loc[dataset[field] == '[]'] = new_class           
            

#%%
def get_dist_cont_values(dataset, field, avoid_class):
    values = dataset.loc[dataset[field] != avoid_class, field]
    
    #df = pd.DataFrame(values)
    return values
    #df.hist()
    #ax = values.hist(bins = 100,alpha=0.5)
    

#%%
def get_stats(dataset, field):
    pass
        


#%%
def find_jump(values):
    
    diff = 0
    prev = values[0]
    prejump = 0
    posjump = 0
    for val in values:
        if(abs(val-prev) > diff):
            diff = abs(val-prev)
            prejump = prev
            posjump = val
        prev = val
    
    return prejump, posjump, diff

#%%
def count_records_in_json(record):
    import json
    
    json_record = json.loads(record)
    return len(json_record)



#%%
def replace_with_len(dataset, field, zero_class):
    for index in range(0,dataset.shape[0]):
        value = dataset.at[index,field]    
        if(value != zero_class):
            count = count_records_in_json(value)
        else:
            count = 0
        dataset.at[index,field] = count



#%%
#def string_matches(strin1, strin2):
#    avoid = ["la", "las", "lo", "los", "a", "al", "el", "de", "del", "con"
#             "para", "por", "que", ]
    




