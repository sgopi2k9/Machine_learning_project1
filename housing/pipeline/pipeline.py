from threading import Thread
from housing.component.data_ingestion import DataIngestion
from housing.component.data_validation import DataValidation
from housing.config.configuration import Configuration
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.exception import HousingException
import os,sys

config = Configuration()

class Pipeline(Thread):


    def __init__(self, config: Configuration = config) -> None:
        try:
            super().__init__(daemon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) \
            -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise HousingException(e, sys) from 