# Importar herramientas
import hackaUtils

# Importar dataset
dt_name = 'Candidates'
dataset = hackaUtils.get_dataset([dt_name])[dt_name]


#%% Seleccionar los campos clave
columns = ['title_or_profession','available_to_move','civil_status','has_video','profile_description','birthdate','identification_type','identification_number','psy_tests','email','first_name','last_name','phone']
filtered_dt = hackaUtils.drop_columns(dataset, columns)

#%% Analisis de variable por variable

# Gender


