# Importar herramientas
import hackaUtils

# Importar datasets
#%%
dt_name = 'Vacants'
vacants_dataset = hackaUtils.get_dataset([dt_name])[dt_name]

#%%
# Eliminar campos
columns = ['expiration_date', 'number_of_quotas', 'max_salary', 'titles_and_studies','knowledge_and_skills', 'experience_and_positions', 'requirements', 'publish_date', 'created_at', 'title', 'description' ]
filtered_dt = hackaUtils.drop_columns(vacants_dataset, columns)


#%%
# Cambiar los NaN en education level
# Reemplazar NaN por undefined
column = 'education_level'
nan_class = 'undefined'
hackaUtils.replace_nan(filtered_dt, column, nan_class)


#%% Exportar a csv
filtered_dt.to_csv(r'filtered_vacants.csv', index = False, header=True)















