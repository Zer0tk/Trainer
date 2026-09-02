from trainee import Trainee


class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2


class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        return True


class Cohort:
    title: str
    trainees: list[Trainee]

    def __init__(self, title: str, trainees: list[Trainee] = []) -> None:
        self.title = title
        self.trainees = trainees


    def add_trainee(self, trainee: Trainee) -> None:
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        passing_students: list[Trainee] = []

        for trainee in self.trainees:
            if trainee.is_passing():
                passing_students.append(trainee)

        return passing_students