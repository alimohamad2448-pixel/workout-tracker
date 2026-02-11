

from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name: str, date: str = None):
        """Initialize an Exercise.
        
        Args:
            name: The name of the exercise
            date: The date performed (defaults to today if not provided)
        """
        # TODO: Set self.name
        # TODO: Set self.date (use datetime.now().strftime("%Y-%m-%d") if date is None)
        
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
    
        self.name = name
        self.date = date 
    
    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self) -> str:
        """Return a string representation of the exercise."""
        # TODO: Return a string like "ExerciseName: 100 calories"
        # Use self.calculate_calories() to get the calories
        return f"{self.name}: {self.calculate_calories()} calories"

class CardioExercise(Exercise):

    def __init__(self, name: str, distance: float, duration: float, date: str = None):

        super().__init__(name, date)
        self.distance = distance
        self.duration = duration


    def calculate_calories(self):

        calories = self.distance * 100
        return calories

    def get_duration(self):

        return self.duration

    def __str__(self):
        return f"{self.name} ({self.distance:.1f} miles, {self.duration:.0f} min): {self.calculate_calories():.0f} calories"


class StrengthExercise(Exercise):
    def __init__(self, name: str, weight: float, reps: int, sets: int, date: str = None):
        
        super().__init__(name, "Pull_ups")
        self.weight = weight
        self.reps = reps
        self.sets = sets

    def calculate_calories(self):
        calories = self.weight * self.reps * self.sets * 0.05
        return calories

    def get_duration(self):
        duration = self.sets * 3
        return duration


    def __str__(self):

        return f"{self.name} ({self.weight} lbs x {self.reps} reps x {self.sets} sets): {self.calculate_calories()} calories"


class FlexibilityExercise(Exercise):
    INTENSITY_MULTIPLIERS = {
        "low": 1.0,
        "medium": 1.5,
        "high": 2.0
    }

    def __init__(self, name: str, duration: float, intensity: str = "medium", date: str = None):
        super().__init__(name, date)

        self.duration = duration

        intensity = intensity.lower()
        if intensity not in self.INTENSITY_MULTIPLIERS:
            raise ValueError(
                f"Invalid intensity '{intensity}'. Must be one of: low, medium, high"
            )
        self.intensity = intensity

    def calculate_calories(self):
        multiplier = self.INTENSITY_MULTIPLIERS[self.intensity]
        return int(self.duration * 2.5 * multiplier)

    def get_duration(self):
        return self.duration

    def __str__(self):
        return f"{self.name} ({self.duration} min, {self.intensity} intensity): {self.calculate_calories()} calories"
    