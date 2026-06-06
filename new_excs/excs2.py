class Starship:
    """A space vessel."""

    ship_type = "Exploration Vessel"

    def __init__(self, name, crew_size):
        self.name = name
        self.crew_size = crew_size

    def set_destination(self, destination):
        return f"{self.name} sets a course for {destination}."

    def __str__(self):
        return f"{self.ship_type} - {self.name}"


class ScienceVessel(Starship):
    
    """A specialized starship for scientific research."""
    
    ship_type = "Science Vessel"
    
    def __init__(self,name,crew_size,labs):
        super().__init__(name,crew_size)
        self.labs=labs
        
    def __str__(self):
        base_str=super().__str__()
        return base_str +  f" | Research labs: {self.labs}"
        
    def survey(self):
        return f"{self.name} surveys the sector."