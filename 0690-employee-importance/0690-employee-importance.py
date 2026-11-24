"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = None
        for e in employees:
            if e.id == id:
                employee = e
                return employee.importance + sum([self.getImportance(employees, a) for a in e.subordinates]) 

        if employee is None:
            return 0
        