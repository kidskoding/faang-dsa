from abc import ABC


# Part 1: model TravelProduct (abstract base) + Hotel, Flight, Activity.
class TravelProduct(ABC):
    pass


class Hotel(TravelProduct):
    pass


class Flight(TravelProduct):
    pass


class Activity(TravelProduct):
    pass


# Part 2: return only Activities strictly cheaper than budget.
def filter_activities(products: list[TravelProduct], budget: float) -> list[Activity]:
    pass


# Part 3: ordered collection of booked Activities that reports total distance.
class Itinerary:
    def __init__(self) -> None:
        pass

    def add_activity(self, activity: Activity) -> None:
        pass

    def total_distance(self) -> float:
        pass


# Part 4: search the mixed collection by optional criteria, sorted by a field.
class SearchEngine:
    def __init__(self, products: list[TravelProduct]) -> None:
        pass

    def search(
        self,
        max_price: float | None = None,
        min_rating: float | None = None,
        product_type: type[TravelProduct] | None = None,
        sort_by: str = "price",
        descending: bool = False,
    ) -> list[TravelProduct]:
        pass
