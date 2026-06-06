class SmartThermostat:
    def __init__(self, serial_no, brand, target_temp):
        # NOTE: We prefix backing variables with an underscore (e.g., _serial_no) 
        # to avoid naming conflicts with the getter/setter property methods.
        self._serial_no = serial_no
        self._brand = brand
        
        # This assignment automatically routes through the @target_temp.setter 
        # method right at initialization, enforcing validation.
        self.target_temp = target_temp

    # --- READ-ONLY PROPERTIES (Getters only) ---

    @property
    def serial_no(self):
        """Getter: Invoked automatically when accessing 'ob.serial_no'."""
        return self._serial_no

    @property
    def brand(self):
        """Getter: Invoked automatically when accessing 'ob.brand'."""
        return self._brand.upper()

    # --- READ/WRITE PROPERTY (Getter + Setter) ---

    @property    
    def target_temp(self):
        """Getter: Invoked automatically when accessing 'ob.target_temp'."""
        return self._target_temp
    
    @target_temp.setter
    def target_temp(self, target_temp):
        """Setter: Invoked automatically on assignment (e.g., ob.target_temp = val)."""
        if target_temp < 5 or target_temp > 35:
            raise ValueError("Temperature out of safe range (5-35°C).")
        self._target_temp = target_temp

# Example Usage
ob = SmartThermostat(1, "abC", 32)

# Printing these attributes implicitly invokes their respective getter methods
print(ob.serial_no, ob.brand, ob.target_temp)