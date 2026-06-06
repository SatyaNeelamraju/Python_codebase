class Starship:
    """A space vessel."""

    ship_type = "Exploration Vessel"

    def __init__(self, name, crew_size):
        """Initialize the starship with a name and crew size."""
        self.name=name
        self.crew_size=crew_size
        ...

    def set_destination(self, destination):
        self.destination=destination
        """Return a string describing the course."""
        return f"{self.name} sets a course for {self.destination}."
        ...

    def __str__(self):
        """Return a string description of the starship."""
        return f"{self.ship_type} - {self.name}"
        ...