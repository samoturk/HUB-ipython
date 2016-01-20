#!/usr/bin/env python
from IPython.display import HTML

class HUB:
    """
    HUB event class
    """
    def __init__(self, version):
        self.full_name = "Heidelberg Unseminars in Bioinformatics"
        self.info = HTML("<p>Heidelberg Unseminars in Bioinformatics are participant-"
            "driven meetings where people with an interest in bioinformatics " 
            "come together to discuss hot topics and exchange ideas and then go "
            "for a drink and a snack afterwards.</p>")
        self.version = version
    def __repr__(self):
        return self.full_name