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
            self.status = False
            self.accuracy = random_no
            print(f"Classification Model training - {self.accuracy}% accuracy. Model training fail.")

        else:
            self.status = True
            self.accuracy = random_no
            print(f"Classification Model training - {self.accuracy}% accuracy. Model training success.")
            

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
    
class Dataset():
    def __init__(self, dataset_name, dataset_size):
        self.dataset_name = dataset_name
        self.dataset_size = dataset_size        
        self._column_names = ['age', 'income', 'gender']

    def summaryAction(self):
        self.loadingAction()
        print(f'Name of dataset: {self.dataset_name}\nSize of dataset: {self.dataset_size}\nColumn names: {self._column_names}')

    def loadingAction(self):
        print(f'Loading dataset {self.dataset_name} with {self.dataset_size} rows...')

    



AI_2 = RegressorModel("OGPT-2", 80, False)
AI_2.trainModel()

            