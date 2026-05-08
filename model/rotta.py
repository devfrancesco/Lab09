from dataclasses import dataclass

@dataclass
class Rotta:
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    media : float

    def __hash__(self):
        return hash((self.ORIGIN_AIRPORT_ID, self.DESTINATION_AIRPORT_ID))

    def __eq__(self, other):
        return (self.ORIGIN_AIRPORT_ID == other.ORIGIN_AIRPORT_ID and
                self.DESTINATION_AIRPORT_ID == other.DESTINATION_AIRPORT_ID)

    def __str__(self):
        return f"{self.ORIGIN_AIRPORT_ID} -> {self.DESTINATION_AIRPORT_ID} - Distanza media: {self.media:.2f}"