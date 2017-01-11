class Department(object):
    """Parent class for all departments

    Methods: __init__, get_name, get_supervisor
    """

    def __init__(self, name, supervisor, employee_count):
        self.name = name
        self.supervisor = supervisor
        self.size = employee_count

    def get_name(self):
        """Returns the name of the department"""
        return self.name

    def get_supervisor(self):
        """Returns the name of the supervisor"""
        return self.supervisor

class HumanResources(Department):
    """Class representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """

    def __init__(self, name, supervisor, employee_count):
        super().__init__(name, supervisor, employee_count)
        self.policies = set()

    def add_policy(self, policy_name, policy_text):
        """Adds a policy, as a tuple, to the set of policies

        Arguments:
            policy_name (string)
            policy_text (string)
        """
        self.policies.add((policy_name, policy_text))

    def get_policy(self):
        return self.policies

class InformationTechnology(Department):
    def __init__(self):
        super().__init__(self, name, supervisor, employee_count)
        self.languages = ()

    def add_devLanguage(self, language_name):
        """Adds a language to the set of languages"""

class Marketing(Department):
    """Class representing Marketing department

    Methods: __init__, add_materials, get_materials
    """
    def __init__(self, name, supervisor, employee_count):
        super().__init__(name, supervisor, employee_count)
        self.materials = ()

    def add_material(self, material_type):
        self.materials.add(material_type)

marketing_department = Marketing("Marketing", "Jami Jackson", 3)

print("{0} is the head of the {1} Department, which has {2} employees".format(marketing_department.supervisor, marketing_department.name, marketing_department.size))

human_resources_dept = HumanResources("Human Resources", "Val Hovendon", 1)
human_resources_dept.add_policy("Code Of Conduct", "Covers employees, board members and volunteers")
human_resources_dept.add_policy("Hours Of Work", "Describes the number of hours full time employees are required to work")

print(human_resources_dept.policies)


CodeOfConduct_policy = {x: y for x, y in human_resources_dept.policies if "Code Of Conduct" in x}
print(type(CodeOfConduct_policy))
for k, v in CodeOfConduct_policy.items():
    print("Please see {0}, to view our {1} policy which has the following desription: {2}".format(human_resources_dept.name, k, v))
