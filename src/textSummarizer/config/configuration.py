from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_directories
from textSummarizer.entity import (DataIngestionConfig)
class ConfigurationManager:
      def __init__(self,
                   config_filepath=CONFIG_FILE_PATH,
                   params_filepath=PARAMS_FILE_PATH):
      #   print()       
        # print("Configuration Loaded")
        PATHHHH = (Path(os.path.join(os.getcwd(),"TextSummarizer",config_filepath)))
        
        self.config = read_yaml(PATHHHH)
        self.params = read_yaml((Path(os.path.join(os.getcwd(),"TextSummarizer",params_filepath))))
        create_directories([self.config.artifacts_root])

      def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
        root_dir=config.root_dir,
        source_URL=config.source_URL,
        local_data_file=config.local_data_file,
        unzip_dir=config.unzip_dir
)
        return data_ingestion_config
