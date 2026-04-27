

# calander class for ease
# sets up empty list as calander
  # ellements are the different tasks that need doing
  # ellements have:: dead line; priority; 'easynes' ; name
    # would like for dead line to only take over when less than week(personal pref) before due
# new tasks added will be directly sortet intoo the existing list.
  # gets rid of the need for a sorting function

#20261230

# final::
# list will be stored in external file to allow easy eccess to other scripts.
  # extra functions for reading and updating the file. 


class Calander:
    def __init__(self, name):
        self.name = name
        self.tasksNum = 0
        self.tasksList = []

        print(f"Calander '{name}' created.")


    def findDate(self, date):
        """Returns the index at which a task with the given deadline should be inserted."""
        tasks = self.tasksList
        for i, task in enumerate(tasks):
            if task.deadline is None or task.deadline >= date:
                return i
        return len(tasks)  # insert at end if no later deadline found
    

    def findTask(self, name):
        for i in range(len(self.tasksList)):
            if self.tasksList[i].name.lower() == name.lower():
                return i
        return 


    def addTask(self, name, deadline=None, priority=5, effort=5):
        newTask = Tasks(name, deadline, priority, effort)

        if self.tasksNum == 0 or deadline is None:
            self.tasksList.append(newTask)
            self.tasksNum += 1
            return

        pos = self.findDate(deadline)
        self.tasksList.insert(pos, newTask)
        self.tasksNum += 1


    def updateFullTask(self, task, name, deadline, priority, effort):
        i = self.findTask(task)
        t = self.tasksList[i]
        t.name = name
        t.deadline = deadline
        t.priotity = priority
        t.effort = effort


    def updateTask(self, task):
        t = self.tasksList[self.findTask(task)]

        print(f"{t} found.")

        while True:
            data = input("Pleas enter the data you want to eddit in the following way or enter 'b' to stop::\n\tname = t1, deadline = 20260312, priority = 5, effort = 5 :: ")
            if data == "b": return
            data = data.lower().split()
            print(data)
            i = 0
            while i < len(data):
                if data[i] == "name":
                    t.name = data[i + 2]
                elif data[i] == "deadline":
                    t.deadline = int(data[i + 2])
                elif data[i] == "priority":
                    t.priority = int(data[i + 2])
                elif data[i] == "effort":
                    t.effort = int(data[i + 2])
                elif data[i] == "b":
                    self.reSort()
                    print(f"{t} updated")
                    return
                i+=1
            self.reSort()
            print(f"{t} updated")


    def reSort(self):
        this = self.tasksList
        i = 0
        while i < self.tasksNum-1:
            if this[i].deadline == None:
                temp = this[i]
                this[i] = this[i+1]
                this[i+1] = temp
                i-=1
            elif this[i+1].deadline == None:
                i+=1
            elif this[i].deadline > this[i+1].deadline:
                temp = this[i]
                this[i] = this[i+1]
                this[i+1] = temp
                i-=1
            else: i+=1
        print(f"{self.tasksList} updated")


class Tasks:
    def __init__(self, name, deadline, priority, effort):
        self.name = name
        self.deadline = deadline
        self.priority = priority
        self.effort = effort

    def __repr__(self):
        return f"Task('{self.name}', deadline={self.deadline}, priority={self.priority}, effort={self.effort})"


# --- Main ---
Main = Calander("Main")

Main.addTask("t1", 20260312)
Main.addTask("t2")
Main.addTask("t3", 20260702)
Main.addTask("t4", 20260102)
print(Main.tasksList)

Main.updateFullTask("t1", "T1", 20260412, 5, 5)
print(Main.tasksList)
Main.updateTask("T1")

'''
Light weight calander organizer.
Stores tasks in a list and sorts said list acording to the deadlines.
    Tasks contain a name, deadline, priority and effort score.
It allows for updating tasks and resceduling them.
'''