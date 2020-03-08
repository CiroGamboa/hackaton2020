# Importar herramientas
import hackaUtils

# Importar dataset
dt_name = 'Candidates'
dataset = hackaUtils.get_dataset([dt_name])[dt_name]


#%% Seleccionar los campos clave
columns = ['title_or_profession','available_to_move','civil_status','has_video','profile_description','birthdate','identification_type','identification_number','psy_tests','email','first_name','last_name','phone','country_birth','salary']
filtered_dt = hackaUtils.drop_columns(dataset, columns)

# Modificar valores en los campos #
#%% Gender
column = 'gender'
props = hackaUtils.count_record_per_class(filtered_dt, column)
# Reemplazar NaN, unknown y other_gender por others
classes = hackaUtils.get_minor_classes(props,2)
group_class = 'others'
hackaUtils.replace_minority_values(dataset = filtered_dt, field = column, classes = classes, new_class = group_class)
# Check distribution again
props = hackaUtils.count_record_per_class(filtered_dt, column)


#%% City
column = 'city'
props = hackaUtils.count_record_per_class(filtered_dt, column)

# Reemplazar NaN y otras ciudades minoritarias por others
classes = hackaUtils.get_minor_classes(props,4)
group_class = 'others'
hackaUtils.replace_minority_values(dataset = filtered_dt, field = column, classes = classes, new_class = group_class)
# Check distribution again
props = hackaUtils.count_record_per_class(filtered_dt, column)







#%% Education level
column = 'education_level'
props = hackaUtils.count_record_per_class(filtered_dt, column)

# Reemplazar NaN por undefined
nan_class = 'undefined'
hackaUtils.replace_nan(filtered_dt, column, nan_class)








#%% Salary
'''
column = 'salary'

# Reemplazar NaN por undefined
nan_class = 'undefined'
hackaUtils.replace_nan(filtered_dt, column, nan_class)
'''

#%% Without experience
column = 'without_experience'
props = hackaUtils.count_record_per_class(filtered_dt, column)




#%% Without studies
column = 'without_studies'
props = hackaUtils.count_record_per_class(filtered_dt, column)


#%% Studies
column = 'studies'
nan_class = 'undefined'
# Cambiar listas vacías por clase 'undefined'
hackaUtils.replace_empty_lists(filtered_dt, column, nan_class)


#%% Studies
column = 'experiences'
nan_class = 'undefined'
# Cambiar listas vacías por clase 'undefined'
hackaUtils.replace_empty_lists(filtered_dt, column, nan_class)