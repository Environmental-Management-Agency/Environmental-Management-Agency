# backend/apps/ai/models.py
from django.db import models
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class WasteClassificationModel(models.Model):
    model = models.BinaryField()
    accuracy = models.FloatField()

    def train_model(self):
        data = WasteManagementData.objects.all()
        X = data.values_list('parameter', flat=True)
        y = data.values_list('value', flat=True)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        self.model = model
        self.accuracy = accuracy
        self.save()
