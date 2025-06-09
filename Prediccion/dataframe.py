import pandas as pd
from .models import Classification, Harvest_Type, Harvest, Harvest_Details
from .serializers import (
    Classification_Serializer,
    Harvest_type_Serializer,
    Harvest_Serializer,
    HarvestDetails_Serializer
)

class Cosecha_Dataframes:

    @staticmethod
    def classification_to_df(preprocessed=False):
        queryset = Classification.objects.all()
        serializer = Classification_Serializer(queryset, many=True)
        df = pd.DataFrame(serializer.data)

        if not preprocessed:
            return df

        # Procesamiento para modelo
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['created_year'] = df['created_at'].dt.year
        df['created_month'] = df['created_at'].dt.month
        
        # Codificar campos categóricos
        df['variety'] = df['variety'].astype('category').cat.codes
        df['classification'] = df['classification'].astype('category').cat.codes

        # Eliminar columnas no útiles o texto libre
        df = df.drop(columns=['details', 'created_at'])
        
        return df


    @staticmethod
    def harvest_type_to_df(preprocessed=False):
        queryset = Harvest_Type.objects.all()
        serializer = Harvest_type_Serializer(queryset, many=True)
        df = pd.DataFrame(serializer.data)

        if not preprocessed:
            return df
        
        # Convertir fechas
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['end_date'] = pd.to_datetime(df['end_date'])
        df['created_at'] = pd.to_datetime(df['created_at'])

        # Extraer características temporales
        df['start_month'] = df['start_date'].dt.month
        df['end_month'] = df['end_date'].dt.month
        df['created_year'] = df['created_at'].dt.year
        
        # Codificar categóricos
        df['name'] = df['name'].astype('category').cat.codes
        df['season'] = df['season'].astype('category').cat.codes
        df['classification'] = df['classification'].astype('int')  # FK: deja ID numérico

        # Eliminar columnas de texto y fechas originales
        df = df.drop(columns=['start_date', 'end_date', 'created_at'])
        
        return df


    @staticmethod
    def harvest_to_df(preprocessed=False):
        queryset = Harvest.objects.all()
        serializer = Harvest_Serializer(queryset, many=True)
        df = pd.DataFrame(serializer.data)

        if not preprocessed:
            return df

        # Fechas
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['created_year'] = df['created_at'].dt.year
        df['created_month'] = df['created_at'].dt.month
        
        # Codificar categóricos
        df['harvest_method'] = df['harvest_method'].astype('category').cat.codes
        df['season'] = df['season'].astype('category').cat.codes
        df['type'] = df['type'].astype('int')  # FK

        # Rellenar nulos
        df['latitude'] = df['latitude'].fillna(0)
        df['longitude'] = df['longitude'].fillna(0)

        # Columnas relevantes
        df = df[['quantity', 'harvest_method', 'type', 'season', 'latitude', 'longitude', 'created_year', 'created_month']]

        return df


    @staticmethod
    def harvest_details_to_df(preprocessed=False):
        queryset = Harvest_Details.objects.all()
        serializer = HarvestDetails_Serializer(queryset, many=True)
        df = pd.DataFrame(serializer.data)

        if not preprocessed:
            return df
        
        # Fechas
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['created_year'] = df['created_at'].dt.year
        df['created_month'] = df['created_at'].dt.month

        # Codificar categóricos
        df['overall_quality'] = df['overall_quality'].astype('category').cat.codes
        df['classification'] = df['classification'].astype('int')  # FK

        # diagram_data es JSON, eliminar o procesar aparte
        df = df.drop(columns=['diagram_data', 'created_at'])
        
        # Columnas útiles
        df = df[['estimated_price', 'profit_margin', 'overall_quality', 'classification', 'created_year', 'created_month']]

        return df
