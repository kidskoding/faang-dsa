# Travel Product Modeling (OOP Design)

Source: OOP / object-modeling design round (Expedia-style)

An object-oriented design problem delivered in four parts. Each part builds on
the previous one

## Part 1

Expedia offers three products: **Hotels**, **Flights**, and **Activities**.

Every product has a `price`, a `rating`, and a `location`. In addition:

- a Hotel has a `room_type`
- a Flight has an `airline`
- an Activity has a `duration`

Design the class structure to represent these products. A search engine holds a
single mixed collection of all three types and filters over them, so the design
should support that cleanly.

## Part 2

Write a method that takes a mixed list of travel products and a budget limit,
and returns only the **Activities** whose price is strictly less than the
budget.

```python
Input:
  products = [Hotel(price=200, ...), Activity(price=50, ...),
              Flight(price=300, ...), Activity(price=120, ...)]
  budget = 100

Output:
  [Activity(price=50, ...)]
```

## Part 3

Design an `Itinerary` class that holds a user's booked **Activities** in
scheduled order and reports the total distance traveled between consecutive
activities across the whole trip.

- Support adding activities incrementally.
- Expose the total distance over the ordered activities (distance between two
  activities is derived from their `location`).

State the data structure backing the itinerary and the time complexity of
adding an activity versus computing the total distance.

## Part 4

Design a `SearchEngine` over the full mixed collection of products. A user
searches with any combination of the following criteria, each optional:

- a maximum price
- a minimum rating
- a product type (Hotels only, Flights only, Activities only, or any)

The engine returns all matching products, sorted by a caller-chosen field
(price or rating) in ascending or descending order.

New product types and new filter or sort fields will be added over time, so the
design should let those be introduced without rewriting the core search logic.
