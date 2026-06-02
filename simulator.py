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

AI_1 = Model("OGPT", 95, False)
AI_1.trainModel()
AI_1.deployModel()
            