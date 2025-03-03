from configparser import ConfigParser

class Config:
    def __init__(self,config_file = "UIConfigFile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    def get_sec1_title(self):
        return self.config["DEFAULT"].get("SECTION_1")
    
    def get_sec2_title(self):
        return self.config["DEFAULT"].get("SECTION_2")
    
    def get_sec3_title(self):
        return self.config["DEFAULT"].get("SECTION_3")