import random 

class Model:

    def __init__(self, name, accuracy, status=False):
        self.name = name
        self.accuracy = accuracy
        self.status = status

    def trainModel(self):
        print(f"Model {self.name} training has been initialized.")
        self.status = True
        return self.status
    
    def evaluateModel(self):
        print("Evaluating Model's performance and accuracy")
    
    def deployModel(self):
        if self.status == True:
            print(f"Model {self.name} is being deployed to a production centre.")
        else:
            print(f"Model {self.name} deployment failed as training has not been initialized.")

class ClassifierModel(Model):
    def __init__(self, name, accuracy, status=False):
        super().__init__(name, accuracy, status)
    
    def trainModel(self):
        print("Training classification model using Cross-Entropy Loss.")
        print("Determining training accuracy...")
        random_no = random.randint(0,100)
        if random_no < 50:
            print(f"Classification Model training - {random_no}% accuracy. Model training fail.")
            self.status = False
        else:
            print(f"Classification Model training - {random_no}% accuracy. Model training success.")
            self.status = True

class RegressorModel(Model):
    def __init__(self, name, accuracy, status=False):
        super().__init__(name, accuracy, status)
    
    def trainModel(self):
        print("Training regression model using Mean Squared Error (MAE).")
        self.status = True
        self.evaluateModel()

    def evaluateModel(self):
        error_rate = round(random.uniform(0.0, 0.25), 2)
        print(f"Regresion Evaluation - Error Rate: {error_rate}")
    



AI_2 = RegressorModel("OGPT-2", 80, False)
AI_2.trainModel()

            