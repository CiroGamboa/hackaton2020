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
    Contar cuantos registros estan en NaN por cada campo
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








