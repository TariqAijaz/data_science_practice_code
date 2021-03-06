#Learn Python for Data Science
#Data Science practice challenge code

from sklearn import tree

classifier = tree.DecisionTreeClassifier()
#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], 
     [181, 85, 43]]

Y = ['male','female','male','male','female','male','female','female','male','female','male']

classifier = classifier.fit(X,Y)

prediction = classifier.predict([[190,70,43]])

print(prediction)

