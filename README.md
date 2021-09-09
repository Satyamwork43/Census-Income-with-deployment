# Census-Income-with-deployment
HEROKU LINK https://censusincomeprediction.herokuapp.com/




https://user-images.githubusercontent.com/78307104/128574782-8bfadee0-b5a1-4726-bec3-8b37711535f5.mp4

# Problem Statement:

This data was extracted from the 1994 Census bureau database by Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics). A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1) && (HRSWK>0)). The prediction task is to determine whether a person makes over $50K a year.

# EDA
# CountPlots
![Screenshot_61](https://user-images.githubusercontent.com/78307104/132678723-ca45bb25-2585-4bf2-9a8b-04d86bbd5155.png)

# Obseravtion
1-From upper graph i can say there are more people who work in private company and very less who work in local-govt and self-emp-not-inc
2-Education-there are more people who have did hs-grad and bachelors and there are also very few people who have did 11th 4th and all 

#Distribution Plot
![Screenshot_1](https://user-images.githubusercontent.com/78307104/132679619-a76f47f4-97f0-4e0d-a22c-ee7aa8642fc3.png)

# Observation
1-only the value of fnlwgt is continuous so that distribution is right skewed so in right skewed we know mean>median>mode

2-for other columns i can say they are discrete

![Screenshot_2](https://user-images.githubusercontent.com/78307104/132679743-c300d029-4c86-4686-9dba-42891446922c.png)
# Obseravtion
1-From age i can say from 25-65 people have high chances to get more then 50k

2-From workclass i can say except without pay and never worked other workclass have chances to earn more then 50k

![Screenshot_3](https://user-images.githubusercontent.com/78307104/132679863-aa5277d6-b83c-4631-a9f7-ea149b70c71e.png)
# Obseravtion 
*people earning >50k income work mean hours per week greater than tose earning

<50k whilw peoplw from both the categories work from min to max hours per week*

![Screenshot_4](https://user-images.githubusercontent.com/78307104/132679947-acb73baf-688c-40b2-9da0-c73a0a885f24.png)

# Obseravtion

the plot shows people belonging to different contries have less chances of earning>50k which is wrong,this is because np.of individuals belonging from other countries other than U.S are very low but it is to be noticed that there are more people in the category <50k than >50k

![Screenshot_6](https://user-images.githubusercontent.com/78307104/132680061-3638baa8-d191-45e8-84fe-b693e205f543.png)

![Screenshot_18](https://user-images.githubusercontent.com/78307104/132680376-9005d4d8-46a7-4ac9-8e1b-abe739b8fb98.png)

#Obseravtion
there are no people after the age of 50 in the married to armed forced category with just a few outliers.

Windowed category has seen icrease as the age seems to increase there are very few widow at early age

![Screenshot_8](https://user-images.githubusercontent.com/78307104/132680546-492189f9-add6-481f-a60f-e8dec8a557ea.png)
# Observation
People who get salary <50k they work more and people who get salary >50k they work less as comapre to other


# Checking Multicollinearity and Correlation
![Screenshot_9](https://user-images.githubusercontent.com/78307104/132680666-fd17c00f-1f86-4f40-9d71-a86e6cc948d1.png)
# Observation
Correlation is seems to be good like education having good +ve correlation and relationship and sex having -ve correlation and rest of the columns are also having correlation but at low level


# Preporcessing 
1-Checking outliers if any i have removed them with percentile method
2-Checking skewness and removed it
3-Feature transformation
4-Feature Scaling

# Model Training 
I have trained many model but Lightgbm was giving me good accuracy 
# Performance Metrics of Lightgbm
![Screenshot_14](https://user-images.githubusercontent.com/78307104/132681199-502dd2df-3a9c-4a32-acaa-f9c50a7fc99d.png)
# Learning Curve of Lightgbm
![Screenshot_16](https://user-images.githubusercontent.com/78307104/132681284-b054a999-902e-4775-ac12-009798f0cf6e.png)

Finally i have deployed my model after hyperparameter tuning using streamlit on heroku

