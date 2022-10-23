"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
 


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    df=df[df.columns[1:]]
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    #Colocamos sexo en minusculas y eliminamos espacios en blanco
    df.sexo=df.sexo.str.lower()

    #para tipo de tipo_de_emprendimiento
    df.tipo_de_emprendimiento=df.tipo_de_emprendimiento.str.lower()
    df.tipo_de_emprendimiento=df.tipo_de_emprendimiento.str.strip()


    #para tipo de idea_negocio
    df.idea_negocio=df.idea_negocio.str.replace('-',' ')
    df.idea_negocio=df.idea_negocio.str.replace('_',' ')
    df.idea_negocio=df.idea_negocio.str.lower()
    df.idea_negocio=df.idea_negocio.str.strip()

    #Barrio
    df.barrio=df.barrio.str.replace('-',' ')
    df.barrio=df.barrio.str.replace('_',' ')
    df.barrio=df.barrio.str.replace('.',' ')
    df.barrio=df.barrio.str.lower()
    df.barrio=df.barrio.str.strip()

    #linea de credito
    df.línea_credito=df.línea_credito.str.replace('-',' ')
    df.línea_credito=df.línea_credito.str.replace(' ','_')
    df.línea_credito=df.línea_credito.str.lower()


    #fecha
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    #print(df.monto_del_credito.value_counts())
    #Monto de credito
    df.monto_del_credito = (df.monto_del_credito.str.replace('[^\d.]+', '', regex=True))
    df.monto_del_credito=df.monto_del_credito.str.strip()
    df.monto_del_credito=df.monto_del_credito.apply(pd.to_numeric, downcast='integer', errors='ignore')

    #print(df[df.estrato==0])
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    print(df.estrato.value_counts())


    return df
    
print(clean_data().sexo.value_counts().to_list())
